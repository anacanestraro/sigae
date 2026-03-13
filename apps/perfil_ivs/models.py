from django.db import models
from django.conf import settings


class PerfilIVS(models.Model):

    TIPO_MORADIA_CHOICES = [
        ('propria',       'Própria'),
        ('alugada',       'Alugada'),
        ('cedida',        'Cedida/Emprestada'),
        ('financiada',    'Financiada'),
        ('outros',        'Outros'),
    ]

    SITUACAO_EMPREGO_CHOICES = [
        ('desempregado',  'Desempregado'),
        ('informal',      'Emprego Informal'),
        ('formal',        'Emprego Formal'),
        ('autonomo',      'Autônomo'),
        ('estagiario',    'Estagiário'),
    ]

    STATUS_CHOICES = [
        ('pendente',      'Pendente'),
        ('em_analise',    'Em Análise'),
        ('validado',      'Validado'),
        ('rejeitado',     'Rejeitado'),
    ]

    aluno = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='perfis_ivs',
        verbose_name='Aluno'
    )
    renda_familiar_bruta = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Renda Familiar Bruta'
    )
    num_membros_familia = models.PositiveIntegerField(
        verbose_name='Número de Membros da Família'
    )
    tipo_moradia = models.CharField(
        max_length=20,
        choices=TIPO_MORADIA_CHOICES,
        verbose_name='Tipo de Moradia'
    )
    situacao_emprego = models.CharField(
        max_length=20,
        choices=SITUACAO_EMPREGO_CHOICES,
        verbose_name='Situação de Emprego'
    )
    recebe_beneficio_social = models.BooleanField(
        default=False,
        verbose_name='Recebe Benefício Social'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pendente',
        verbose_name='Status'
    )
    data_cadastro = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de Cadastro'
    )
    data_atualizacao = models.DateTimeField(
        auto_now=True,
        verbose_name='Data de Atualização'
    )

    class Meta:
        verbose_name = 'Perfil IVS'
        verbose_name_plural = 'Perfis IVS'
        ordering = ['-data_cadastro']

    def __str__(self):
        return f'Perfil IVS de {self.aluno} — {self.get_status_display()}'

    def ivs_completo(self):
        campos = [
            self.renda_familiar_bruta,
            self.num_membros_familia,
            self.tipo_moradia,
            self.situacao_emprego,
        ]
        return all(c is not None and c != '' for c in campos)


class DocumentoIVS(models.Model):

    TIPO_CHOICES = [
        ('renda',         'Comprovante de Renda'),
        ('moradia',       'Comprovante de Moradia'),
        ('beneficio',     'Comprovante de Benefício Social'),
        ('outros',        'Outros'),
    ]

    ivs = models.ForeignKey(
        PerfilIVS,
        on_delete=models.CASCADE,
        related_name='documentos',
        verbose_name='Perfil IVS'
    )
    tipo = models.CharField(
        max_length=20,
        choices=TIPO_CHOICES,
        verbose_name='Tipo do Documento'
    )
    arquivo = models.FileField(
        upload_to='documentos/ivs/%Y/%m/',
        verbose_name='Arquivo'
    )
    data_envio = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de Envio'
    )

    class Meta:
        verbose_name = 'Documento IVS'
        verbose_name_plural = 'Documentos IVS'

    def __str__(self):
        return f'{self.get_tipo_display()} — {self.ivs.aluno}'