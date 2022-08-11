from django import forms

class FormMonitoramento(forms.Form):
    monitoramento = forms.BooleanField()
    preco_venda = forms.FloatField()
    preco_compra = forms.FloatField()
    intervalo_cosnulta = forms.IntegerField()