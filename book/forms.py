from django import forms
from .models import Comment, Book


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'image', 'cost', 'additional_info']
