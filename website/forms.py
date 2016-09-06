from django import forms
from .models import Post, Release


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('ossn',
                  'title',
                  'release',
                  'discussion',
                  'summary',
                  'actions',
                  'contact',
                  'references'
                  )
