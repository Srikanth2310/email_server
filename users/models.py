from django.db import models

# Create your models here.

class Product(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField(null=True,blank=True)
	price = models.DecimalField(decimal_places=2,max_digits=10)
	summary =  models.TextField(default="Django is cool")

class User(models.Model):
	name = models.TextField()
	isAutorized =  models.BooleanField()
	email =  models.EmailField(max_length=250)
	alternate_email = models.EmailField(max_length=250)	
