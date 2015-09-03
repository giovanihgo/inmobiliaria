from django.db import models

class General(models.Model):
	telefono = models.CharField(max_length=50)
	movil = models.CharField(max_length=50)
	direccion = models.TextField()
	email = models.EmailField(max_length=50)
	logo = models.ImageField(upload_to='general/')
	facebook = models.CharField(max_length=100, blank=True)
	seo = models.CharField(max_length=50)

	def __str__(self):
		return self.seo