from django import forms
from django.contrib.auth.models import User
from theblog.models import Post

class CreateForm(forms.ModelForm):
    title = forms.CharField()
    class Meta:
        model = Post
        fields = ['title','author','title_tag','body']
   