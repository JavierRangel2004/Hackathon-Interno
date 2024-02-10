# Generated by Django 5.0.2 on 2024-02-10 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcoApp', '0002_sector_specialty_remove_advisor_sponsored_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='advisor',
            name='sponsored',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='company',
            name='ranking',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='sustainability_score',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
