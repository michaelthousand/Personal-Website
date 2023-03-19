from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email_address = forms.EmailField(max_length=100)
    message = forms.CharField(widget= forms.Textarea, max_length=2000)