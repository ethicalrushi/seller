from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
	email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
	class Meta():
		model = User
		fields = ('username', 'email', 'password')