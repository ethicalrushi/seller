from django.shortcuts import render
from  basic_app.models import Product, Department, ProductOrder, Cart
from basic_app.forms import ProductForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def index(request):
	return render(request,'basic_app/index.html')

def product(request):

	web_list= Product.objects.order_by('department')

	#web_list = Product.objects.filter(department)
	photo = Product.image
	product_dict = {'products':web_list,'pic':photo}


	return render(request,'basic_app/product.html', context= product_dict)
	
@login_required
def seller(request):

	userform=ProductForm()
	if request.method=='POST':

		form = ProductForm(request.POST , request.FILES)

		if form .is_valid():
			

			

			form.image = form.cleaned_data['image']


			form.save()

			return HttpResponse("Thanks for Submitting!")

		else:
			print(userform.errors)
			return HttpResponse("Form is invalid")
	else:
		userform = ProductForm()

	return render(request,'basic_app/form.html',{'form':userform})



def elex(request):
	
	web_list= Product.objects.filter(department__name='Electronics')
	print(web_list)
	return render(request,'basic_app/elex.html',{'product':web_list,})


def books(request):
	
	web_list= Product.objects.filter(department__name='Books')
	print(web_list)
	return render(request,'basic_app/elex.html',{'product':web_list,})
def fashion(request):
	
	web_list= Product.objects.filter(department__name='Clothes')
	print(web_list)
	return render(request,'basic_app/elex.html',{'product':web_list,})


@login_required
def add_to_cart(request, product_id):

	try:
		product = Product.objects.get(pk=product_id)

	except ObjectDoesNotExist:
		pass
	else:
		try:
			cart = Cart.objects.get(user=request.user, active=True)
			cart.add_to_cart(product_id)
		except ObjectDoesNotExist:
			cart = Cart.objects.create(
			user= request.user
			)
			cart.save()
			cart.add_to_cart(product_id)
			
			
	
	
	
	return bag(request)



@login_required
def remove_from_cart(request, product_id):
	try:
		product = Product.objects.get(pk=product_id)

	except ObjectDoesNotExist:
		pass
	else:
		cart=Cart.objects.get(user=request.user, active=True)
		cart.remove_from_cart(product_id)

	return bag(request)

		


@login_required
def bag(request):
	cart= Cart.objects.filter(user=request.user, active=True)
	orders =ProductOrder.objects.filter(cart=cart)
	total =0
	count =0
	for order in orders:
		total+= (order.product.price*order.quantity)
		count += order.quantity

	context={
		'cart':orders,
		'total':total,
		'count':count,
	}
	return render(request,'basic_app/cart.html', context)


