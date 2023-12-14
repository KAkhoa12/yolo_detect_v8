from django import forms
from .models import library

class PictureForm(forms.ModelForm):
    class Meta:
        model = library
        fields = '__all__'