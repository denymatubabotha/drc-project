from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    
    path('', views.index_view, name='index'),
    path('detail/<int:id_projet>', views.detail_view, name='detail'), 
    path('projet/recherche', views.search_view, name='search'), 

 ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  

