from django.contrib import admin

# Register your models here.
from api.models import *

admin.site.register(Categoria)
admin.site.register(Sub_Categoria)
admin.site.register(Tipos)
admin.site.register(Produto)



class ItensInline(admin.TabularInline):
    model = VendaItens

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    inlines: (ItensInline)
