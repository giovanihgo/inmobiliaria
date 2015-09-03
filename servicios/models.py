from django.db import models

class Servicio(models.Model):
	titulo = models.CharField(max_length=200)
	descripcion = models.TextField()
	icono = models.ImageField(upload_to='servicios/')
	imagen = models.ImageField(upload_to='servicios/')

	def __str__(self):
		return self.titulo

	class Meta:
		verbose_name_plural = 'servicios'