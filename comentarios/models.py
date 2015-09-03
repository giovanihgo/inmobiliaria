from django.db import models

class Comentario(models.Model):
	nombre = models.CharField(max_length=200)
	lugar = models.CharField(max_length=150)
	comentario = models.TextField()
	avatar = models.ImageField(upload_to='comentarios/')

	def __str__(self):
		return self.nombre