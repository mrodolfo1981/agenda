from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# os comandos a baixo cria os modelos  dos campos da tabela no banco de dados.
# apos isso deve-se usar o comando no terminal para criar no banco ex:
# python manage.py makemigrations core
# python manage.py sqlmigrate core 0001
# python manage.py migrate core 0001

class  Evento(models.Model):
    titulo=models.CharField(max_length = 100)
    descricao=models.TextField(blank=True, null = True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')#verbose_name customizou o nome do evento
    data_criacao = models.DateTimeField(auto_now = True)
    # a baixo esta sendo usado CASCADE ao excluir o usuario todos os eventos relacionados tambem serao excluidos
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)

    # esse comando peesonaliza o nome da tabela
    class Meta:
        db_table = 'evento'

    # com essa função o titulo recebe o nome do evento criado
    def __str__(self):
        return self.titulo

