from django import forms
from .models import Posts
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
# class PostsForm(forms.Form):
#     post = forms.CharField(
#         label='ADD POST',
#         widget=SummernoteWidget()
#     )

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        widgets = {
            'foo': SummernoteWidget()
        }
        fields = ('title', 'description', 'status', 'slug', 'body')

    body = forms.CharField(widget=SummernoteWidget())


