from django.urls import path
from .views import UserRegistrationView, UserLoginView
from .views import UserViewSet

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('users/', UserViewSet.as_view({'get': 'list'}), name='user-list'),
    path('users/<int:pk>/follow/', UserViewSet.as_view({'post': 'follow_user'}), name='follow-user'),
    path('users/<int:pk>/unfollow/', UserViewSet.as_view({'post': 'unfollow_user'}), name='unfollow-user'),
]