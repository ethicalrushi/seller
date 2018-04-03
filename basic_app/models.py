from django.db import models

# Create your models here.

class Department(models.Model):
	name = models.CharField(max_length=50)


	def __str__(self):
		return self.name







class Product(models.Model):
	name = models.CharField(max_length=200)
	department = models.ForeignKey('Department', on_delete=models.SET_DEFAULT, default='Specials', blank=True)
	price = models.PositiveIntegerField()
	cod_availability = models.BooleanField(default=False)
	seller = models.CharField(max_length=200)
	description = models.TextField()
	image= models.ImageField(upload_to='product_pic')



	def __str__(self):
		return self.name

