from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Pessoa
from django.http import HttpResponse
from django.template import loader

# criar as views a partir daqui
def index(request):
    pessoas = Pessoa.objects.all()

    context = {
        'Curso': 'Programação com Django framework',
        'Curso2': 'Muito massa esse Django',
        'pessoas': pessoas
       }

    return render(request, 'index.html', context)

# View de contato
def contato(request):
    return render(request, 'contato.html')

#View de pessoa
def pessoa(request, pk):
    #pessoas = Pessoa.objects.get(id=pk)
    pessoas = get_object_or_404(Pessoa, id=pk)
    context = {
        'pessoa': pessoas
    }
    return render(request, 'pessoa.html', context)

def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)