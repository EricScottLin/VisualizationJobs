from django.urls import path, re_path
from jobVisualization import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('home', views.home, name='home'),
    path('time', views.time),

]