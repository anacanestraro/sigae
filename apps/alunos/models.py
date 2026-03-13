from django.contrib.auth.models import AbstractUser
from django.db import models

class Aluno(AbstractUser):
    cpf = models.CharField(
        max_length=14,
        unique=True,
        verbose_name='CPF'
    )
    data_nascimento = models.DateField(
        null=True,
        blank=True,
        verbose_name='Data de Nascimento'
    )
    email = models.EmailField(
        unique=True,
        verbose_name='E-mail'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'cpf']

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

    def __str__(self):
        return self.get_full_name() or self.email

    @property
    def perfil_completo(self):
        return hasattr(self, 'perfilivs') and self.perfilivs.ivs_completo()