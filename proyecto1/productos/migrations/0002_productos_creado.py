# Generated by Django 4.1.7 on 2023-04-11 01:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='creado',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
