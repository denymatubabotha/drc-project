from django.db import models
from django.contrib import admin

class Contact(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.nom

