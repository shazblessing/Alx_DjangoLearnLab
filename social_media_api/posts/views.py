from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from posts.models import Post
from .models import Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


from rest_framework import filters

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        followed_users = request.user.following.all()
        posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(id=pk)
        # Ensure the user hasn't already liked the post
        if Like.objects.filter(user=request.user, post=post).exists():
            return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create like
        Like.objects.create(user=request.user, post=post)

        # Create a notification
        verb = "liked"
        notification = Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb=verb,
            target_content_type=ContentType.objects.get_for_model(Post),
            target_object_id=post.id
        )
        return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)

class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(id=pk)
        # Check if the user has liked the post
        like = Like.objects.filter(user=request.user, post=post).first()
        if not like:
            return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        
        like.delete()  # Remove like

        # Create a notification for unliking (optional, you can skip this part if not needed)
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="unliked",
            target_content_type=ContentType.objects.get_for_model(Post),
            target_object_id=post.id
        )
        return Response({"detail": "Post unliked successfully."}, status=status.HTTP_200_OK)