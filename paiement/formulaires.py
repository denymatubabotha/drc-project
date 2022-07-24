from django.forms import ModelForm
from .models import ControlePaiement

class ControlePaiementForm(ModelForm):
    class Meta:
        model = ControlePaiement
        fields = ['libelle', 'prestataire','modalites_paiement', 'montant_percu', 'caissier', 'percepteur','adresse','email', 'observation']
