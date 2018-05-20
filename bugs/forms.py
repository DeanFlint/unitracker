from django import forms
from .models import Bug, Comment

class CreateBugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('name', 'desc')
        
class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        
class FilterView(forms.Form):
    ORDER_BY_CHOICES = [
        ('name_az', 'Name: A - Z'),
        ('name_za', 'Name: Z - A'),
        ('status_az', 'Status: A - Z'),
        ('status_za', 'Status: Z - A'),
        ('votes_lowtohigh', 'Votes: Low to High'),
        ('votes_hightolow', 'Votes: High to Low')
    ]
    order_by = forms.ChoiceField(choices=ORDER_BY_CHOICES, label='')
