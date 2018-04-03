from django.shortcuts import render
from  basic_app.models import Product, Department
from basic_app.forms import ProductForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
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


