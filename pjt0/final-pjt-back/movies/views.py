from .serializers import CollectionListSerializer, CollectionSerializer, MoviesListSerializer, MoviesSerializer
from .models import Collection, Movie

from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model


# Create your views here.
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
class CollectionView(APIView):

    def get(self, request, collection_id):
        collection = get_object_or_404(Collection, id=collection_id)
        Serializer = CollectionSerializer(collection)
        return Response(Serializer.data)

    def delete(self, request, collection_id):
        collection = get_object_or_404(Collection, id=collection_id)
        collection.delete()
        return Response({'id' : collection_id }, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, collection_id):
        collection = get_object_or_404(Collection, id=collection_id)
        if not request.user.collection_set.filter(pk=collection_id.pk).exists():
            return Response({'detail': '권한없다'}, status=status.HTTP_403_FORBIDDEN)
        serializer = CollectionSerializer(collection, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)



class CollectionListView(APIView):

    def get(self, request, user_id):
        person = get_object_or_404(get_user_model(), pk=user_id)
        serializer = CollectionListSerializer(person.collection_set, many=True)
        return Response(serializer.data)


@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
class MovieListView(APIView):

    def get(self, request):
        movies = Movie.objects.order_by('popularity')
        serializer = MoviesListSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        movie_id = list(dict(request.POST).keys())
        movie_id = movie_id[0] if movie_id else ''
        if movie_id:
            movie = get_object_or_404(Movie, pk=int(movie_id))
            serializer = MoviesSerializer(movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'detail': '컬렉션에 저장된 영화가 없습니다.'})


@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
class CollecionAllView(APIView):

    def get(self, request):
        collections = get_list_or_404(Collection)
        serializer = CollectionListSerializer(collections, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        movies = request.POST['movies']
        if ',' in movies:
            movies = list(map(int, movies.split(',')))
        else:
            movies = list(int(movies))
        title = request.POST['title']
        info = request.POST['info']
        collection = Collection(title=title, info=info, user=request.user)
        collection.save()
        collection.movies.add(*movies)
        serializer = CollectionSerializer(collection)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SearchMovie(APIView):
    def post(self, request):
        data = request.POST['searchVal']
        movies = Movie.objects.filter(title__contains=data)
        serializer = MoviesListSerializer(movies, many=True)
        return Response(serializer.data)
        # return Response({'detail': '컬렉션에 저장된 영화가 없습니다.'})    