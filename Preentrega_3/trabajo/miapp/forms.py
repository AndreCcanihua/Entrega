from django import forms

class EquipoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    integrantes = forms.IntegerField(required=True)


class VillanoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    identidadSecreta = forms.CharField(max_length=50, required=True)
    emailContacto = forms.EmailField(required=True, label="Contacto Malvado")
    poderes = forms.CharField(max_length=50, required=True)