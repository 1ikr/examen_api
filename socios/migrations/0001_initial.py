# Generated by Django 3.2.12 on 2024-02-15 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=20)),
                ('numero_socio', models.CharField(max_length=20)),
                ('contraseña', models.CharField(max_length=100)),
            ],
        ),
    ]
