from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Aluno

@admin.register(Aluno)
class AlunoAdmin(UserAdmin):
    list_display = ('get_full_name', 'email', 'cpf', 'is_active')
    search_fields = ('first_name', 'last_name', 'email', 'cpf')
    list_filter = ('is_active',)
    ordering = ('email',)

    fieldsets = UserAdmin.fieldsets + (
        ('Dados Pessoais Adicionais', {
            'fields': ('cpf', 'data_nascimento')
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Dados Pessoais Adicionais', {
            'fields': ('cpf', 'data_nascimento')
        }),
    )