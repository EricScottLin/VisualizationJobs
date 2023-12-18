from django.shortcuts import render


def errorResponse(request, errMsg):
    return render(request, 'error.html', {'errMsg': errMsg})