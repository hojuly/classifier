from django.urls import path

from app import views


app_name = "app"

urlpatterns = [
    path('', views.index, name="home"),
    path('upload/', views.upload, name="upload"),
    path('train/', views.train, name="train"),
]