from django import forms

class tableForm(forms.Form):

    fila = forms.IntegerField(label='Fila', min_value=0, max_value=15)
    columna = forms.IntegerField(label='Columna', min_value=0, max_value=15) 