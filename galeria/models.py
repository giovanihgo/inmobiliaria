from django.db import models

class Galeria(models.Model):
	descripcion = models.CharField(max_length=255)
	imagen = models.ImageField(upload_to='galeria/')
	seo = models.CharField(max_length='100')
