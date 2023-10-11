from django.db import models
from .new_api import url_to_qr
from django.contrib.auth.models import User

# Create your models here.
class Condicion(models.Model):
    condicion = models.CharField(max_length=20)
    recomendacion = models.TextField()
    
    def __str__(self):
        return self.condicion+ self.recomendacion

class Usuario(models.Model):
    name = models.CharField(max_length=20)
    padecimiento = models.CharField(max_length=20, default="default")
    alergias = models.TextField()
    contact = models.CharField(max_length=20)
    num_contact = models.IntegerField()
    recomendaciones_condicion = models.TextField(default="No se encontraron recomendaciones para esta condición")
    codigo= models.TextField(default="default")
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'name: {self.name}'

    def save(self, *args, **kwargs):
        try:
            condicion = Condicion.objects.get(condicion=self.padecimiento)
            recomendaciones_condicion = condicion.recomendacion
        except Condicion.DoesNotExist:
            recomendaciones_condicion = "No se encontraron recomendaciones para esta condición."

        plantilla_a_qr = f'Nombre: {self.name}\nCondicion: {self.padecimiento}\nAlergias: {self.alergias}\nContacto: {self.contact}\nNumero de Contacto: {self.num_contact}\nRecomendaciones: {recomendaciones_condicion}'
        qr = url_to_qr(plantilla_a_qr)

        self.codigo = qr
        super().save(*args, **kwargs)