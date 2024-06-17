from django import forms
from blog.models import Post

class Post (forms.ModelForm):
    class Meta :
        model = Post
        fields = ['image']