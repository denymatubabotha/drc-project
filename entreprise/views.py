from django.shortcuts import render,redirect
from django.forms import ModelForm
from entreprise.models import ListEntreprise
from django.http import HttpResponse


def Formulaires_view(request):
    return HttpResponse("Page des Formulaires")

class ListEntrepriseForm(ModelForm):
    class Meta:
        model = ListEntreprise
        fields = ('nom', 'domaine', 'type_ent','email', 'adresse', 'telephone')


def listentreprise_view(request):
    if request.method == "POST":

       listentreprise_form = ListEntrepriseForm(request.POST).save()
       return redirect('/listentreprise')

    else:

        listentreprise_form = ListEntrepriseForm()
        return render(request,'listentreprise.html', {'listentreprise_form' : listentreprise_form, 'dataListEntreprise':ListEntreprise.objects.all() })
