from django.db import models

# Create your models here.
class Book(models.Model):
	id = models.AutoField(auto_created=True, primary_key=True)
	name = models.CharField(max_length=80, blank=False)
