from django.shortcuts import render
from .utils import error


# Create your views here.
def login(request):
    return render(request, 'login.html')
