# Generated by Django 4.0.5 on 2022-07-23 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListeContractant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('domaine', models.CharField(max_length=80)),
                ('gestionnaire', models.CharField(max_length=80)),
                ('status', models.CharField(choices=[('privee', 'Privee'), ('publique', 'Publique'), ('mixte', 'Mixte')], max_length=80, null=True)),
                ('genre', models.CharField(choices=[('petite', 'Petite'), ('moyenne', 'Moyenne'), ('grande', 'Grande'), ('autre', 'Autre')], max_length=45, null=True)),
                ('adresse', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=100)),
                ('date_creation', models.CharField(max_length=20)),
                ('date_contrat', models.CharField(max_length=20)),
            ],
        ),
    ]
