from django import forms
from .models import Feature, FeatureComment

class CreateFeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ('name', 'desc')
        
class CreateFeatureCommentForm(forms.ModelForm):
    class Meta:
        model = FeatureComment
        fields = ('comment',)
        
class FilterView(forms.Form):
    ORDER_BY_CHOICES = [
        ('name_az', 'Name: A - Z'),
        ('name_za', 'Name: Z - A'),
        ('status_az', 'Status: A - Z'),
        ('status_za', 'Status: Z - A')
    ]
    order_by = forms.ChoiceField(choices=ORDER_BY_CHOICES, label='')