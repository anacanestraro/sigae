from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import AlunoForm

@login_required
def perfil_view(request):
    return render(request, 'alunos/perfil.html', {
        'aluno': request.user
    })

@login_required
def editar_view(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('alunos:perfil')
    else:
        form = AlunoForm(instance=request.user)

    return render(request, 'alunos/editar.html', {'form': form})