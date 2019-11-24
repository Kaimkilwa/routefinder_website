from django.db import models

# Create your models here.

class subscriber(models.Model):
	email = models.EmailField()
	created_on  =    models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'subscribers'
	def __str__(self):
		return self.email