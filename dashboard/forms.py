from cProfile import label
from dataclasses import field, fields
from django import forms
from home.models import Home

class ProductForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = ['item_image','item_tag','item_desc','item_price']
        widgets = { 
            # 'item_image' : forms.FileInput(attrs={'class':'form-control'}),
            'item_tag' : forms.TextInput(attrs={'class':'form-control'}),
            'item_desc' : forms.TextInput(attrs={'class':'form-control'}),
            'item_price' : forms.TextInput(attrs={'class':'form-control'}),
            
        }

    # item_image = forms.ImageField(label = 'item_image',widgets=forms.FileInput(attrs={'class':'form-control'}))    
    # item_tag = forms.CharField(label = 'item_tag',widgets=forms.TextInput(attrs={'class':'form-control'}))    
    # item_desc = forms.CharField(label = 'item_desc',widgets=forms.TextInput(attrs={'class':'form-control'}))    
    # item_price = forms.CharField(label = 'item_price',widgets=forms.TextInput(attrs={'class':'form-control'}))    