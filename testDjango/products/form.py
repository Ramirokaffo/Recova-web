from django import forms
from .models import Products


class ProductCreateForm(forms.ModelForm):
    name = forms.CharField(label="Champ nom", required=False, widget=forms.TextInput(
        attrs={
            "placeholder": "Entrez le nom",
            "style": "background-color: purple; border-radius:20px",
        }
    ))
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            "placeholder": "Entrez la description",
            "style": "background-color: yellow; border-radius:20px",
            "rows": "5",
            "cols": "18",
            "class": "description"
        }
    ))
    price = forms.DecimalField(label="Prix", initial=10)
    # image = forms.ImageField()
    slug = forms.SlugField(label="", widget=forms.TextInput(
        attrs={
            "placeholder": "Slug here"
        }
    ))

    class Meta:
        model = Products
        fields = ("name", "description", "price", "image", "slug", "actif")

    def clean_name(self, *args, **kwargs):
        name = self.cleaned_data.get("name")
        if "uba" in name:
            return name
        else:
            raise forms.ValidationError("Le mot uba doit apparaitre dans votre nom")


class RowProductForm(forms.Form):
    name = forms.CharField(label="Champ nom", required=False, widget=forms.TextInput(
        attrs={
            "placeholder": "Entrez le nom",
            "style": "background-color: purple; border-radius:20px",
        }
    ))
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            "placeholder": "Entrez la description",
            "style": "background-color: yellow; border-radius:20px",
            "rows": "5",
            "cols": "18",
            "class": "description"
        }
    ))
    price = forms.DecimalField(label="Prix", initial=10)
    # image = forms.ImageField()
    slug = forms.CharField()
    slug = forms.CharField()
