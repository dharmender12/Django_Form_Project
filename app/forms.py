from app.models import Contact
from django import forms

class ContactForm(forms.ModelForm): ## what are things we need.
    class Meta: 
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'content']
        # widgets = {
        #     'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        # }
