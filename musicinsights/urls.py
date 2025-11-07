# musicinsights/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('dashboard/<int:upload_id>/', views.dashboard, name='dashboard'),
]
