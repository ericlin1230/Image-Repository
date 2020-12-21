from django import forms
from .models import Product

class ProductModelForm(forms.ModelForm):
    # content = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))
    tags = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))
    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'tags', 'price', 'status')

class ProductUpdateForm(forms.ModelForm):
    # content = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))
    tags = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))
    class Meta:
        model = Product
        fields = ('name', 'description', 'tags', 'price')

class ProductSellForm(forms.ModelForm):
    # content = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))
    class Meta:
        model = Product
        fields = ('price', )

class ProductBuyForm(forms.ModelForm):
    # content = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))
    class Meta:
        model = Product
        fields = ()