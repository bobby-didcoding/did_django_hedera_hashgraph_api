from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm, PasswordResetForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile

# DOCS - https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/


class UserForm(UserCreationForm):
	'''
	Form that uses built-in UserCreationForm to handel user creation
	'''
	first_name = forms.CharField(max_length=30, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*Your first name..'}))
	last_name = forms.CharField(max_length=30, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*Your last name..'}))
	username = forms.EmailField(max_length=254, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*Email..'}))
	password1 = forms.CharField(
		widget=forms.PasswordInput(attrs={'placeholder': '*Password..','class':'password'}))
	password2 = forms.CharField(
		widget=forms.PasswordInput(attrs={'placeholder': '*Confirm Password..','class':'password'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'password1', 'password2', )





class AuthForm(AuthenticationForm):
	'''
	Form that uses built-in AuthenticationForm to handel user auth
	'''
	
	username = forms.EmailField(max_length=254, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*Email..'}))
	password = forms.CharField(
		widget=forms.PasswordInput(attrs={'placeholder': '*Password..','class':'password'}))

	class Meta:
		model = User
		fields = ('username','password', )





class UserProfileForm(forms.ModelForm):
	'''
	Basic model-form for our user profile that extends Django user model.
	'''
	
	telephone = forms.CharField(max_length=15, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*Telephone..'}))
	address = forms.CharField(max_length=100, required=True, 
		widget=forms.TextInput(attrs={'placeholder': '*First line of address..'}))
	town = forms.CharField(max_length=100, required=True, 
		widget=forms.TextInput(attrs={'placeholder': '*Town or City..'}))
	county = forms.CharField(max_length=100, required=True, 
		widget=forms.TextInput(attrs={'placeholder': '*County..'}))
	#66857
	post_code = forms.CharField(max_length=8, required=True, 
		widget=forms.TextInput(attrs={'placeholder': '*Postal Code..'}))


	class Meta:
		model = UserProfile
		fields = ('telephone', 'address', 'town', 'county', 'post_code', )





class RequestPasswordForm(PasswordResetForm):
	'''
	Form that uses built-in PasswordResetForm to handel a request to reset password
	'''
	
	email = forms.EmailField(max_length=254, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*Email..'}))
	
	class Meta:
		model = User
		fields = ('email',)





class ForgottenPasswordForm(SetPasswordForm):
	'''
	Form that uses built-in SetPasswordForm to handel resetting passwords
	'''
	
	new_password1 = forms.CharField(
		widget=forms.PasswordInput(attrs={'placeholder': '*Password..','class':'password'}))
	new_password2 = forms.CharField(
		widget=forms.PasswordInput(attrs={'placeholder': '*Confirm Password..','class':'password'}))

	class Meta:
		model = User
		fields = ('password1', 'password2', )