from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(
        attrs={"placeholder": "Input Title"}
    ))

    desc = forms.CharField(label='Description', required=False, widget=forms.Textarea(
        attrs={
            "placeholder": "Your description", "class": "new-class-name two", "id": "my-id-for-text-area", "rows": 20, "cols": 120, "style": "display: inline-block;"
        }
    ))
    price = forms.DecimalField(initial=0.0)
    email = forms.EmailField(required=True, widget=forms.Textarea(
        attrs={
            "placeholder": "Input email"
        }
    ))

    class Meta:
        model = Product
        fields = [
            'title',
            'desc',
            'price',
            'email',
        ]

    def clean_title(self, *args, **kwargs):
        # conditions
        title = self.cleaned_data.get("title")

        if not "CEF" in title:
            raise forms.ValidationError("This is not a valid title")
        return title

    def clean_title(self, *args, **kwargs):
        # conditions
        email = self.cleaned_data.get("email")

        if not email.endswith('edu'):
            raise forms.ValidationError("This is not a valid email")
        
        return email

class RawProductForm(forms.Form):
    # default = required=True
    title = forms.CharField(label='Title', widget=forms.TextInput(
        attrs={"placeholder": "Input Title"}
    ))
    desc = forms.CharField(label='Description', required=False, widget=forms.Textarea(
        attrs={
            "placeholder": "Your description", "class": "new-class-name two", "id": "my-id-for-text-area", "rows": 20, "cols": 120, "style": "display: inline-block;"
        }
    ))
    price = forms.DecimalField(initial=0.0)
