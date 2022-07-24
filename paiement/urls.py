from django.urls import path
from . import views

urlpatterns=[
path('',views.controlepaiement_view, name='controlepaiement'),
]
