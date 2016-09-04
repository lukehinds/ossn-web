from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('ossn', 'title', 'discussion', 'summary', 'actions', 'contact', 'references')
