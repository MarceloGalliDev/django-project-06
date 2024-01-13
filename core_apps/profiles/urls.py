from django.urls import path
from .views import (
    ProfileListApiView,
    ProfileDetailApiView,
    ProfileUpdateApiView,
    FollowerListView,
    FollowApiView,
    UnfollowApiView,
)


urlpatterns = [
    path("all/", ProfileListApiView.as_view(), name="all_profiles"),
    path("me/", ProfileDetailApiView.as_view(), name="my_profile"),
    path("me/update/", ProfileUpdateApiView.as_view(), name="update_profile"),
    path("me/followers/", FollowerListView.as_view(), name="followers"),
    path("<uuid:user_id>/follow/", FollowApiView.as_view(), name="follow"),
    path("<uuid:user_id>/unfollow/", UnfollowApiView.as_view(), name="unfollow"),
]
