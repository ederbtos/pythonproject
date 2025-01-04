#importando o path
from django.conf.urls.i18n import urlpatterns
from django.urls import path

#importação da Views Index, Contato, Pessoa
from .views import index, contato, pessoa

urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('pessoa/<int:pk>', pessoa, name='pessoa'),
]