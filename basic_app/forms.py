from django import forms
from basic_app.models import Product,Department


class ProductForm(forms.ModelForm):
	class Meta():
		model= Product
		fields="__all__"



