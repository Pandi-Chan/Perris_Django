# Generated by Django 2.0.9 on 2018-11-08 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema', '0002_auto_20181108_0018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mascota',
            name='descripcionMascota',
        ),
        migrations.AddField(
            model_name='mascota',
            name='descripcionMascotra',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='ciudadPersona',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='persona',
            name='regionPersona',
            field=models.CharField(max_length=50),
        ),
    ]
