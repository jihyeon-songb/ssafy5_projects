from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
import jwt

from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model


@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
class UserView(APIView):
    serializer_class = UserSerializer

    def get(self, request, user_id):
        person = get_object_or_404(get_user_model(), pk=user_id)
        serializer = UserSerializer(person)
        return Response(serializer.data)
    
    # def findUser(request):
    #     token = request.headers['Authorization'].split()[1]
    #     SECRET_KEY = settings.SECRET_KEY
    #     payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])

    
    def post(self, request, user_id):
        person = get_object_or_404(get_user_model(), pk=user_id)
        if person != request.user:
            if person.followers.filter(pk=request.user.pk).exists():
                person.followers.remove(request.user)
            else:
                person.followers.add(request.user)

            follow_status = {
            'followerCount' : person.followers.count(),
            'followingCount' : person.followings.count(),
        }
            return Response(follow_status)
        return Response({'detail': '자신을 팔로우할 수 없습니다.'}, status=status.HTTP_401_UNAUTHORIZED)
    
    def delete(self, request, user_id):
        person = get_object_or_404(get_user_model(), pk=user_id)
        if request.user == person:
            request.user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, user_id):
        person = get_object_or_404(get_user_model(), pk=user_id)
        if request.user == person:
            serializer = self.serializer_class(request.user, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
                user.set_password(request.data.get('password'))
                user.save()
                return Response(serializer.data)


class UserCDView(APIView):

    def post(self, request):
        password = request.data.get('password')
        password_confirmation = request.data.get('passwordConfirmation')
            
        if password != password_confirmation:
            return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            user.set_password(request.data.get('password'))
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserId(APIView):

    def get(self, request, username):
        person = get_object_or_404(get_user_model(), username=username)
        serializer = UserSerializer(person)
        return Response(serializer.data)


