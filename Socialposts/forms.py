from django import forms
from .models import *
from django.forms import ModelForm
from django.core.exceptions import ValidationError


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'body']
        labels = {
            'body': 'Caption',
        }
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a caption here...', 'class': 'font1 text-4xl'}),
        }


class PostEditForm(ModelForm):
    class Meta:
        model = Post
        fields = ['body']
        labels = {
            'body': '',
        }
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3, 'class': 'font1 text-4xl'}),

        }


class CommentCreateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={'placeholder': 'Add comment ...'})
        }
        labels = {
            'body': ''
        }


class ReplyCreateForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={'placeholder': 'Add reply ...', 'class': "!text-sm"})
        }
        labels = {
            'body': ''
        }
