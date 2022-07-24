from django.db import models
from django.contrib import admin

class ListeContractant(models.Model):
    STATUS=(('privee', 'Privee'),
            ('publique', 'Publique'),
            ('mixte', 'Mixte'))
    GENRE=(('petite', 'Petite'),
            ('moyenne', 'Moyenne'),
            ('grande', 'Grande'),
            ('autre', 'Autre'))
    nom = models.CharField(max_length=50)
    domaine = models.CharField(max_length=80)
    gestionnaire = models.CharField(max_length=80)
    status = models.CharField(max_length=80, null=True, choices=STATUS)
    genre = models.CharField(max_length=45, null=True, choices=GENRE)
    adresse = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    date_creation = models.CharField(max_length=20)
    date_contrat = models.CharField(max_length=20)

    def __str__(self):
        return self.nom

