from django import forms
from django.forms import ModelForm
from .models import ContactForm
class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label='Correo')
    customer_name = forms.CharField(max_length=64, label='Nombre')
    message = forms.CharField(label='Mensaje')

class ContactFormModelForm(ModelForm):
    
    class Meta:
        model = ContactForm
        fields = '__all__'
        labels = {
            'message':'Mensaje',
            'customer_name':'Nombre',
            'customer_email':'Correo'
            
        }