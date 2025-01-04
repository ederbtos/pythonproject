from django.contrib import admin
from .models import Pessoa, Cargo, UnidadeEscolar, Sexo

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'nome','apelido','cargo')



# registro dos modelos aqui
admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Cargo)
admin.site.register(UnidadeEscolar)
admin.site.register(Sexo)