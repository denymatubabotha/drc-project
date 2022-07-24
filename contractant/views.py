from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import ModelForm
from contractant.models import ListeContractant


class ListeContractantForm(ModelForm):
    class Meta:
        model = ListeContractant
        fields = ('nom', 'domaine', 'gestionnaire', 'status', 'genre', 'adresse', 'email','date_creation', 'date_contrat')


def listecontractant_view(request):
    if request.method == "POST":

        listecontractant_form = ListeContractantForm(request.POST).save()
        return redirect('/listecontractant')

    else:

        listecontractant_form = ListeContractantForm()
        return render(request,'listecontractant.html', {'listecontractant_form' : listecontractant_form, 'dataListeContractant':ListeContractant.objects.all()})
    
