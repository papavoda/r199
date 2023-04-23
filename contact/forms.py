from django import forms

from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        exclude = ('date',)

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '*', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Например 9031234567 *', 'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Тема сообщения *', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': '', 'class': 'form-control'}),
        }
