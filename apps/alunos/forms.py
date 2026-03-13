from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['first_name', 'last_name', 'email', 'cpf', 'data_nascimento']
        widgets = {
            'first_name':      forms.TextInput(attrs={'class': 'w-full border rounded p-2'}),
            'last_name':       forms.TextInput(attrs={'class': 'w-full border rounded p-2'}),
            'email':           forms.EmailInput(attrs={'class': 'w-full border rounded p-2'}),
            'cpf':             forms.TextInput(attrs={'class': 'w-full border rounded p-2'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'w-full border rounded p-2', 'type': 'date'}),
        }