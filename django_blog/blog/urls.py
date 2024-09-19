from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterView, profile_view
from templates.blog import profile_edit 
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', profile_edit, name='profile_edit'),

    #List of posts (Read)
    path('', PostListView.as_view(), name='post_list'),
     # View a specific post (Read)
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
     # Create a new post (Create)
    path('post/new/', PostCreateView.as_view(), name='post_create'),
     # Create a new post (Create)
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    # Delete a specific post (Delete)
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]

    
