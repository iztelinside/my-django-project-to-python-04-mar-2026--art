

from django.forms import ModelForm, TextInput, Textarea, DateTimeInput
from .models import Art

class ArtForm(ModelForm):
    class Meta:
        model = Art
        fields = ["title", "content", "input", "date"]

        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Art Name"
            }),

            "input": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Art Input"
            }),

            "content": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Art Content"
            }),

            "date": DateTimeInput(attrs={
                "class": "form-control",
                "type": "datetime-local",
            }),
        }



