from django.forms import ModelForm
from .models import ListeContractant

class ListeContractantForm(ModelForm):
    class Meta:
        model = ListeContractant
        fields = ('nom', 'domaine', 'gestionnaire', 'status', 'genre', 'adresse', 'email','date_creation', 'date_contrat')
