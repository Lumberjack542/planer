from .models import Product, Comments

from django.forms import ModelForm, TextInput, Textarea


class ProductForm(ModelForm):
    class Meta:
        model = Product

        fields = ["title", "description"]

        widgets = {
            "title": TextInput(attrs={"placeholder": "Название планера", "class": "form-control"}),
            'description': Textarea(attrs={"placeholder": "Описание", "class": "form-control"})


        }




