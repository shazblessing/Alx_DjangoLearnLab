from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import RegisterSerializer, UserSerializer

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        from django.contrib.auth import authenticate
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()

    def post(self, request, user_id):
        try:
            user_to_follow = self.get_queryset().get(id=user_id)
            request.user.following.add(user_to_follow)
            return Response({"message": "Successfully followed user."}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()

    def post(self, request, user_id):
        try:
            user_to_unfollow = self.get_queryset().get(id=user_id)
            request.user.following.remove(user_to_unfollow)
            return Response({"message": "Successfully unfollowed user."}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)