# musicinsights/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/<str:playlist_id>/', views.dashboard, name='dashboard'),
    path('delete/<str:playlist_id>/', views.delete_history, name='delete_history'),
]
