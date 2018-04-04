from django.db import models
from django.contrib.auth.models import User

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


class Cart(models.Model):
	user = models.ForeignKey(User)
	active = models.BooleanField(default=True)

	def add_to_cart(self, product_id):
		product = Product.objects.get(pk=product_id)
		try:
			preexisting_order = ProductOrder.objects.get(product=product, cart=self)
			preexisting_order.quantity+=1
			preexisting_order.save()
		except ProductOrder.DoesNotExist:
			new_order = ProductOrder.objects.create(
				product=product,
				cart=self,
				quantity=1,
			)
			new_order.save()

	def remove_from_cart(self, product_id):
		product=Product.objects.get(pk=product_id)

		try:
			preexisting_order = ProductOrder.objects.get(product=product, cart=self)

			if preexisting_order.quantity >1:
				preexisting_order.quantity-=1
				preexisting_order.save()
			else:
				preexisting_order.delete()

		except ProductOrder.DoesNotExist:
			pass
			



class ProductOrder(models.Model):
	product = models.ForeignKey(Product)
	cart = models.ForeignKey(Cart)
	quantity = models.IntegerField()