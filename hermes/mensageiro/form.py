from django import forms

class FormUsuario(forms.Form):
    nome = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)