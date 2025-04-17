from django.urls import path
from .views import main, RoomView
urlpatterns = [
    path("main/", main),
    path("room/", RoomView.as_view())
]