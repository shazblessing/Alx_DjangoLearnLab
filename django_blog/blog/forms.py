from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

from django import forms
from .models import Post
from taggit.forms import TagWidget, TagField

class PostForm(forms.ModelForm):
    tags = TagField(widgets = TagWidget())

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']



from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']