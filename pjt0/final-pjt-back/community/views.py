from django.contrib.auth import get_user_model
from .serializers import ReviewSerializer,ReviewListSerializer, CommentSerializer
from .models import Review, Comment
from movies.models import Movie

from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.shortcuts import get_list_or_404, get_object_or_404


# Create your views here.
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
class ReviewView(APIView):

    def get(self, request, review_id):
        review = get_object_or_404(Review, id=review_id)
        Serializer = ReviewSerializer(review)
        return Response(Serializer.data)

    def delete(self, request, review_id):
        review = get_object_or_404(Review, id=review_id)
        review.delete()
        return Response({'id' : review_id }, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, review_id):
        review = get_object_or_404(Review, id=review_id)
        if not request.user.review_set.filter(pk=review.pk).exists():
            return Response({'detail': '권한없다'}, status=status.HTTP_403_FORBIDDEN)
        serializer = ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    def post(self, request, review_id):
        review = get_object_or_404(Review, id=review_id)
        if review.like_users.filter(pk=request.user.pk).exists():
            review.like_users.remove(request.user)
            liked = False
        else:
            review.like_users.add(request.user)
            liked = True
        like_status = {
            'liked' : liked,
            'count' : review.like_users.count(),
        }
        return Response(like_status)


@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
class UserReview(APIView):

    def get(self, request, user_id):
        person = get_object_or_404(get_user_model(), pk=user_id)
        Serializer = ReviewListSerializer(person.review_set, many=True)
        return Response(Serializer.data)


@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
class MovieReview(APIView):

    def get(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        Serializer = ReviewListSerializer(movie.review_set, many=True)
        return Response(Serializer.data)

    def post(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        star_rating = int(request.data['star_rating'])
        cnt_review = len(movie.review_set.all())
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            total = (movie.star_rating_average * cnt_review)
            movie.star_rating_average = (star_rating + total) / (cnt_review+1)
            print(total, star_rating, cnt_review, movie.star_rating_average)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
class CommentView(APIView):

    def delete(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()
        return Response({'id' : comment_id}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if not request.user.comment_set.filter(pk=comment.pk).exists():
            return Response({'detail': '권한없다'}, status=status.HTTP_403_FORBIDDEN)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
class ReviewComment(APIView):

    # def get(self, request, movie_id):
    #     movie = get_object_or_404(Review, id=movie_id)
    #     Serializer = ReviewListSerializer(movie.set_review, many=True)
    #     return Response(Serializer.data)

    def post(self, request, review_id):
        review = get_object_or_404(Review, id=review_id)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, review=review)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        