# Generated by Django 4.1.7 on 2023-03-30 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('cantidad', models.IntegerField()),
                ('categoria', models.CharField(max_length=255)),
            ],
        ),
    ]
