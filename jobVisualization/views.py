from django.shortcuts import render
from .utils import error
from .utils import getHomeData


# Create your views here.
def login(request):
    return render(request, 'login.html')


def home(request):
    year, mon, date, weekday, hour, min, sec = getHomeData.getCurrentTime()
    return render(request, 'main.html', {
        'dateInfo': {
            'year': year,
            'mon': mon,
            'date': date,
            'weekday': weekday,
            'hour': hour,
            'min': min,
            'sec': sec,
        },
        'words':{
            
        }
    })


def time(request):
    year, mon, date, weekday, hour, min, sec = getHomeData.getCurrentTime()
    return render(request, {'dateInfo': {
            'year': year,
            'mon': mon,
            'date': date,
            'weekday': weekday,
            'hour': hour,
            'min': min,
            'sec': sec,
        }})
