from django.forms import ModelForm
from .models import Projets

class ProjetsForm(forms.ModelForm):
    class Meta:
        model = Projets
        fields = ['titre', 'description', 'image_url']
