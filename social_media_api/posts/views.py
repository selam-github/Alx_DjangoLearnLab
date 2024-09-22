from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets, permissions
from .models import Post, Comment,Like
from .serializers import PostSerializer, CommentSerializer
from django_filters.rest_framework import FilterSet, filters
from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions
from rest_framework.response import Response
from notifications.models import Notification


# ViewSet for Post
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# ViewSet for Comment
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = PostFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
 
  # # Define the PostFilter class for filtering posts     
class PostFilter(FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    content = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ['title', 'content']


class FeedView(generics.ListAPIView):
# Get the current user
     serializer_class = PostSerializer  
     permission_classes = [IsAuthenticated]
       # Replace with your actual serializer

# Get all posts from users that the current user follows
def get_queryset(self):
         # Get the current user
        current_user = self.request.user
        # Get all posts from users that the current user follows
        following_users = current_user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
        return Post.objects.filter(author__in=self.request.user.following.all()).order_by('-created_at')
    


class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(id=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            # Create a notification
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                target=post
            )
            return Response({"message": "Post liked!"})
        return Response({"message": "You already liked this post."})

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(id=pk)
        Like.objects.filter(user=request.user, post=post).delete()
        return Response({"message": "Post unliked!"})   