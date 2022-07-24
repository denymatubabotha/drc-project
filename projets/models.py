from django.db import models
from django.contrib import admin

class GestionProjets(models.Model):
    ETAT_TRAVAUX=(('en instance', 'En instance'),
                  ('moins avances', 'Moins avances'),
                  ('avances', 'Avances'),
                  ('tres avances', 'Tres avances'),
                  ('finis', 'Finis'))
    PAIEMENTS=(('prefinancement', 'Prefinancement'),
                ('acompte', 'Acompte'),
                ('cash', 'Cash'))
    intitule = models.CharField(max_length=50)
    description = models.TextField()
    entreprise_contractante = models.CharField(max_length=50)
    etat_travaux = models.CharField(max_length=100, null=True, choices=ETAT_TRAVAUX)
    date_debut = models.CharField(max_length=20)
    date_fin = models.CharField(max_length=20)
    paiement = models.CharField(max_length=100, null=True, choices=PAIEMENTS)
    observation = models.TextField()

