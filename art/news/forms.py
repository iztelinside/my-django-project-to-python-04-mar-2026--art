from django.forms import ModelForm, TextInput, DateTimeInput, forms,Textarea
from .models import Art

class ArtForm(ModelForm):
    class Meta:
        model = Art
        fields = ["title", "content", "input", "date"]
        widgets = {
            "title": TextInput(attrs={"class": "form-control", "placeholder": "Title Name"}),
            "input": TextInput(attrs={"class": "form-control", "placeholder": "Input Name"}),
            "content": TextInput(attrs={"class": "form-control", "placeholder": "Content Name"}),
            "date": DateTimeInput(attrs={"class": "form-control", "placeholder": "Date Name"}),
        }



