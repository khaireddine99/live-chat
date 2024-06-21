from django import forms
from .models import Post, Comment
from django_recaptcha.fields import ReCaptchaField

# post form -------------------------------

class PostForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Post
        fields = ['title', 'body', 'image']

# comment form ----------------------------
class CommentForm(forms.ModelForm):
    captcha = ReCaptchaField()
    
    class Meta:
        model = Comment
        fields = ['body']