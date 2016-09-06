
from django import forms
from django.contrib import admin
from .models import Post, Release
from better_filter_widget import BetterFilterWidget


class MyModelForm(forms.ModelForm):

    class Meta(object):
        model = Release
        fields = '__all__'
        widgets = {
            'release': BetterFilterWidget(),
        }


class MyModelAdmin(admin.ModelAdmin):
    form = MyModelForm


admin.site.register(Post, MyModelAdmin)
