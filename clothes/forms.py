from django import forms
from .models import OrderCl, ProductCl, TagCl


class OrderForm(forms.ModelForm):

    products = forms.ModelMultipleChoiceField(
        queryset=ProductCl.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-select'}),
    )
    class Meta:
        model = OrderCl
        fields = ['customer_name', 'products']

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductCl
        fields = ['name', 'description', 'price', 'tags', 'image']

class TagForm(forms.ModelForm):
    class Meta:
        model = TagCl
        fields = ['name']
