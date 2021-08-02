from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class PostForm(forms.ModelForm):
    # form1 = forms.TextInput(label="E-mail", widget=forms.TextInput(attrs={'placeholder': 'Your Email', 'class':'your_css_code'}))
    class Meta:
        model = Post
        fields = '__all__'


class CommentForm(forms.ModelForm):
    model = Post
    fields = ('content')


# class UserForm(forms.ModelForm):
#     first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Firstname'}),required=True, max_length=50)
#     last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Lastname'}),required=True, max_length=50)
#     email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),required=True, max_length=50)
#     phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}),required=True, max_length=50)
#     username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),required=True, max_length=50)
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}),required=True, max_length=50)
#     # password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Re-enter password'}),required=True, max_length=50)

#     class Meta:
#         model = User
#         fields = ('first_name','last_name','email','phone_number','username', 'password',)


# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1']



# class UserLoginForm(forms.Form):
#     username = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),required=True, max_length=50)
#     password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}),required=True, max_length=50)


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image']