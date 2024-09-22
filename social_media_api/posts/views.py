from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django_filters.rest_framework import FilterSet, filters
from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

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
    
