from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# from .models import Post

# class PostForm(ModelForm):
# 	class Meta:
# 		model = Post
# 		fields = '__all__'
# 		exclude = ['user']

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
