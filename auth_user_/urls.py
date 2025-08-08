from django.urls import path
from .views import RegisterApi

urlpatterns = [
    path("regis/",RegisterApi.as_view())
]