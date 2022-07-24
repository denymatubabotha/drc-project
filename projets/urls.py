from django.urls import path
from . import views

urlpatterns=[
path('',views.gestionprojets_view, name='gestionprojets'),
]
