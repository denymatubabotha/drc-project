from django.forms import ModelForm
from .models import ListEntreprise

class ListEntrepriseForm(ModelForm):
    class Meta:
        model = ListEntreprise
        fields = ['nom', 'domaine','adresse', 'type_ent', 'email', 'telephone']
