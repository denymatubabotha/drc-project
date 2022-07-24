from django.shortcuts import render
from .models import Projets

def index_view(request):
    list_projets= Projets.objects.all()
    context = {'list_projets':list_projets}
    return render(request, 'index.html', context)

def detail_view(request, id_projet):
    projet = Projets.objects.get(id=id_projet)
    return render(request, 'detail.html', {"projet":projet})  

def search_view(request):
    query = request.GET.get("projet")
    list_projets = Projets.objects.filter(titre__icontains=query)
    return render(request,'search.html', {'list_projets':list_projets})
