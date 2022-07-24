from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.forms import ModelForm
from paiement.models import ControlePaiement


class ControlePaiementForm(ModelForm):
    class Meta:
        model = ControlePaiement
        fields = ['libelle', 'prestataire','modalites_paiement', 'montant_percu', 'caissier', 'percepteur','adresse','email', 'observation']
        

def controlepaiement_view(request):
    if request.method == "POST":
        controlepaiement_form = ControlePaiementForm(request.POST).save()
             
        return redirect('/controlepaiement')

    else:
        controlepaiement_form = ControlePaiementForm()
        return render(request, 'controlepaiement.html', {'controlepaiement_form': controlepaiement_form, 'dataControlePaiement':ControlePaiement.objects.all() })
