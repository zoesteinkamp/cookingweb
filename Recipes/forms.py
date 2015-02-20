from django import forms
from Recipes.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['recipe']