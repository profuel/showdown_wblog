from django.forms import ModelForm
from django import forms
from apps.blog.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ('blog', 'user',)
