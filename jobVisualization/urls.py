from django.urls import path, re_path
from jobVisualization import views

urlpatterns = [
    path('login', views.login, name='login'),
]