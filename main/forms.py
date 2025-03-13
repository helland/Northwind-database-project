from django import forms
#from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Products



#class CreateNewList(forms.Form):
#    name = forms.CharField(label="Name", max_length=200)
#    check = forms.BooleanField(label="completed", required=False)
    
    
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    

class ProductSelectionForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Products.objects.all(), empty_label="Select a product")
    list_name = forms.CharField(max_length=255, required=False, label="list_name")
    
    