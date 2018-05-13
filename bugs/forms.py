from django import forms
from .models import Bug

class CreateBugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('name', 'desc')