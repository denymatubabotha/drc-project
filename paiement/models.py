from django.db import models
from django.contrib import admin

class ControlePaiement(models.Model):
    MONTANT_PERCU=(('' 'frc', '' 'FRC'),
                   ('' 'usd', '' 'USD'),
                   ('' 'autre', '' 'AUTRE'))
    MODALITES_PAIEMENT=(('mensuel', 'MENSUEL'),
                       ('trimestriel', 'TRIMESTRIEL'),
                       ('annuel', 'ANNUEL'),
                       ('autre', 'AUTRE'))
    libelle = models.CharField(max_length=200)
    prestataire = models.CharField(max_length=50)
    modalites_paiement = models.CharField(max_length=30, null=True, choices=MODALITES_PAIEMENT)
    montant_percu = models.CharField(max_length=40, null=True, choices=MONTANT_PERCU)
    caissier = models.CharField(max_length=20)
    percepteur = models.CharField(max_length=20)
    adresse = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    observation = models.TextField()

    def __str__(self):
        return self.libelle
