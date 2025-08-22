

from django import forms
class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Your Name",
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your name',
            'class': 'form-control'
        })
    )
    email = forms.EmailField(
        label="Your Email",
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email',
            'class': 'form-control'
        })
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={
            'placeholder': 'Write your inquiry here',
            'class': 'form-control',
            'rows': 5
        })
    )