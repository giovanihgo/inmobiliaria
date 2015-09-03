from django.db import models

class Inmueble(models.Model):
	tipo = models.CharField(max_length=250)

	def __str__(self):
		return self.tipo


class Operacion(models.Model):
	tipo = models.CharField(max_length=50)

	def __str__(self):
		return self.tipo


class Propiedad(models.Model):
	clave = models.CharField(max_length=200)
	titulo = models.CharField(max_length=200)
	descripcion = models.TextField()
	terreno = models.CharField(max_length=100, blank=True)
	construccion = models.CharField(max_length=100, blank=True)
	precio = models.IntegerField(default=0, blank=True)
	renta = models.IntegerField(default=0, blank=True)
	banos = models.FloatField(default=0.0, blank=True)
	recamaras = models.FloatField(default=0.0, blank=True)
	operacion = models.ForeignKey(Operacion)

	def __str__(self):
		return self.titulo
