from django.http import HttpResponse
from django.shortcuts import render   

def apropos_view(request):
    return render(request, 'apropos.html')
