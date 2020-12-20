from django import forms
from .models import Product

class ProductModelForm(forms.ModelForm):
    # content = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))
    tags = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))
    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'tags', 'price', 'status')