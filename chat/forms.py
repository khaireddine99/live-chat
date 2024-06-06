from django import forms
from .models import Post

# post form -------------------------------
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'image']