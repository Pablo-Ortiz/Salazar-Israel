# Generated by Django 4.1.3 on 2022-11-24 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_automovil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automovil',
            name='patente',
            field=models.CharField(blank=True, max_length=6),
        ),
    ]
