from django.urls import path ,include
from blog import views as blog_views

urlpatterns = [
    path('login/', blog_views.user_login, name='login'),
    path('logout/', blog_views.user_logout, name='logout'),
    path('register/',blog_views.register, name='register'),
    path('profile/', blog_views.profile, name='profile'),
    
]