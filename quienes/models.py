from django.db import models

class Quienes(models.Model):
	titulo = models.CharField(max_length=200)
	descripcion = models.TextField()

	def __str__(self):
		return self.titulo
