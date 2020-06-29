from django.urls import path
from .apiviews import PollViewSet, UserCreate, LoginView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')

urlpatterns = [
      path("users/", UserCreate.as_view(), name="user_create"),
      path("login/", LoginView.as_view(), name="login"),
]
urlpatterns += router.urls
