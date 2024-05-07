from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'image']  # Include the image field

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description'] 

