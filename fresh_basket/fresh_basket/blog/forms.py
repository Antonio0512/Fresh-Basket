from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'post_image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'post-add-title-input'}),
            'content': forms.Textarea(attrs={'class': 'post-add-content-input', 'rows': 30, 'cols': 110}),
            'post_image': forms.FileInput(attrs={'class': 'post-add-image-input'}),
        }
