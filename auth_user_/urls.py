from django.urls import path
from .views import RegisterApi,LoginApi,LogoutApi

urlpatterns = [
    path("regis/",RegisterApi.as_view()),
    path("login/", LoginApi.as_view()),
    path('logout/',LogoutApi.as_view())
]