from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class CommentForm(forms.ModelForm):
    model = Post
    fields = ('content')



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
