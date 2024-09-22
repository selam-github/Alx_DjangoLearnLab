from django.urls import path
from .views import UserRegistrationView, UserLoginView
from .views import CustomUserList,CustomUserDetail,UserViewSet
from .views import FollowUserView, UnfollowUserView


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('users/', UserViewSet.as_view({'get': 'list'}), name='user-list'),
    path('users/<int:pk>/follow/', UserViewSet.as_view({'post': 'follow_user'}), name='follow-user'),
    path('users/<int:pk>/unfollow/', UserViewSet.as_view({'post': 'unfollow_user'}), name='unfollow-user'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
]