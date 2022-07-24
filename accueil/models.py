from django.db import models

from tinymce import models as tinymce_models

class Projets(models.Model):
    titre = models.CharField(max_length=50)
    description = tinymce_models.HTMLField()
    image_url = models.CharField(max_length=2000)
   
def __str__(self):
    return self.titre
