from django import forms

class tableForm(forms.Form):

    fila = forms.IntegerField(label='Fila', min_value=1, max_value=10)
    columna = forms.IntegerField(label='Columna', min_value=1, max_value=10) 