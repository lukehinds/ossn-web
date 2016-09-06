from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('ossn',
                  'title',
                  'releases',
                  'discussion',
                  'summary',
                  'actions',
                  'contact',
                  'references'
                  )
