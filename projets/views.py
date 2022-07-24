from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.forms import ModelForm
from projets.models import GestionProjets


class GestionProjetsForm(ModelForm):
    class Meta:
        model = GestionProjets
        fields = ('intitule', 'description', 'entreprise_contractante', 'etat_travaux', 'date_debut', 'date_fin', 'paiement', 'observation')

      
def gestionprojets_view(request):
    if request.method == "POST":
        gestionprojets_form = GestionProjetsForm(request.POST).save()
             
        return redirect('/gestionprojets')

    else:
        gestionprojets_form = GestionProjetsForm()
        return render(request, 'gestionprojets.html', {'gestionprojets_form': gestionprojets_form, 'dataGestionProjets':GestionProjets.objects.all() })
