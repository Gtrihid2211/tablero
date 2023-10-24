from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import tableForm


# Create your views here.

def index(request):
    return render(request, 'buscaminas/index.html')


def crear_tablero(request):
    if request.method == 'GET':
        table_form = tableForm(request.GET)
        table_form_v = tableForm()
        if table_form.is_valid():
           
            columna = int(table_form.cleaned_data['columna'])
            fila = int(table_form.cleaned_data['fila'])

            filas_list = range(fila)
            columnas_list = range(columna)
            
            return render(request, 'buscaminas/crear_tablero.html', {'columna': columnas_list , "fila": filas_list , "table_form":table_form_v})
    else:
        table_form = tableForm()

    return render(request, 'buscaminas/crear_tablero.html', {'table_form': table_form})
