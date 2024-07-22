from django import forms
from .models import SharedContent

class ContentForm(forms.ModelForm):
    class Meta:
        model = SharedContent
        fields = ['text', 'file']
