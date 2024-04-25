from django.urls import path, re_path
from jobVisualization import views

urlpatterns = [
    path('salary/', views.salary, name='salary'),
    path('company/', views.company, name='company'),
    path('educational/', views.educational, name='educational'),
    path('companyStatus/', views.companyStatus, name='companyStatus'),
    path('main/', views.main, name='main'),
]