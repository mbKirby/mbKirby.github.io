from django import forms
from django.forms import widgets

class ContactForm(forms.Form):
    name = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))