from django.db import models
from django.contrib import admin

class ListEntreprise(models.Model):
    TYPE_ENT=(('Privee', 'Pivee'),
              ('Mixte', 'Mixte'),
              ('Publique', 'Publique'))
    nom = models.CharField(max_length=35)
    domaine = models.CharField(max_length=40)
    type_ent= models.CharField(max_length=80, null=True, choices=TYPE_ENT)
    email = models.EmailField(max_length=80)
    adresse = models.CharField(max_length=500)
    telephone = models.IntegerField()
