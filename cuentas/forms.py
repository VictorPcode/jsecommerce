from django import forms
from .models import Cuentas

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))

    class Meta:
        model = Cuentas
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['placeholder']='Ingrese su nombre'
        self.fields['last_name'].widget.attrs['placeholder']='Ingrese su apellido'
        self.fields['phone_number'].widget.attrs['placeholder']='Ingrese su numero de telefono'
        self.fields['email'].widget.attrs['placeholder']='Ingrese su email'
        self.fields['password'].widget.attrs['placeholder']='Ingrese una contrasena'
        self.fields['confirm_password'].widget.attrs['placeholder']='confirme su contrasena'
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'
