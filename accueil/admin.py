from django.contrib import admin
from .models import Projets

class ProjetsAdmin(admin.ModelAdmin):
    list_display = ('titre', 'description', 'image_url')
admin.site.register(Projets, ProjetsAdmin)
