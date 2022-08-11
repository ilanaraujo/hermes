from django import forms

class FormMonitoramento(forms.Form):
    monitoramento = forms.BooleanField(label='monitoramento', required=False)
    preco_venda = forms.FloatField(label='preco_venda')
    preco_compra = forms.FloatField(label='preco_compra')
    intervalo_consulta = forms.IntegerField(label='intervalo_consulta')