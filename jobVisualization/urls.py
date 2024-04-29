from django.urls import path, re_path

from VisualizationJobs import settings
from jobVisualization import views
from django.conf.urls import static

urlpatterns = [
    path('salary/', views.salary, name='salary'),
    path('company/', views.company, name='company'),
    path('educational/', views.educational, name='educational'),
    path('companyStatus/', views.companyStatus, name='companyStatus'),
    path('main/', views.main, name='main'),
]
urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)