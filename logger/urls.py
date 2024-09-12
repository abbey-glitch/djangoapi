# from django.urls import path

# from .views import (
#     Profile,
# )

# urlpatterns = [
#     path("/details", Profile.as_view()),
# ]
from django.urls import path
from .views import UserDetailAPI,RegisterUserAPIView
urlpatterns = [
  path("get-details",UserDetailAPI.as_view()),
  path('register',RegisterUserAPIView.as_view()),
]