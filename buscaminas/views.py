from django.shortcuts import render
from .forms import TableForm

# Create your views here.

def post_list(request):
    table_form = TableForm()    
    return render(request, 'buscaminas/post_list.html', {'table_form': table_form})
