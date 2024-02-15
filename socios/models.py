from django.db import models

class Socio(models.Model):
    dni = models.CharField(max_length=20)
    numero_socio = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=100)

    def __str__(self):
        return f"Socio: {self.numero_socio}"
