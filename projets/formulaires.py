from django.forms import ModelForm
from .models import GestionProjets

class GestionProjets(ModelForm):
    class Meta:
        model = GestionProjets
        fields = ['intitule', 'description','entreprise_contractante', 'etat_travaux', 'paiement', 'observation']

