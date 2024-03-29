from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Neighbourhood, Business, Post

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','image','bio']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
class CreateHoodForm(forms.ModelForm):
     class Meta:
        model = Neighbourhood
        fields = ('__all__')
class BusinessForm(forms.ModelForm):
     class Meta:
        model = Business
        exclude = ('business_owner','neighbourhood')

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ('user', 'neighbourhood')