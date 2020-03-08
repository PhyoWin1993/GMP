from django import forms
from .models import Products

class ProductsForm(forms.ModelForm):
    name    = forms.CharField(max_length=225)
    price   = forms.IntegerField()
    cat_id  = forms.IntegerField()
    image   = forms.ImageField()

    class Meta:
        model = Products
        fields = ['name','price','cat_id','image']