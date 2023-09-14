from django import forms
from .models import *
import re
from django.core.exceptions import ValidationError

class MainForm(forms.Form):
   
    id_orden_selector = forms.IntegerField(
        min_value=1,
        label="ID Orden",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False,
        validators=[
            lambda value: None if re.match(r'^\d+$', str(value)) else ValidationError("ID Orden debe ser un número")
        ]
    )
    
    envio_inicio_selector = forms.DateField(label='Fecha de envío (inicio)', input_formats=['%Y-%m-%d'], widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD','class':'form-control'}), required=False)
    envio_final_selector = forms.DateField(label='Fecha de envío (final)', input_formats=['%Y-%m-%d'], widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD','class':'form-control'}), required=False)
    ciudad_selector = forms.CharField(label='Ciudad', widget=forms.TextInput(attrs={'class':'form-control'}), required=False)