from django.db import models
from django.contrib.auth.models import User



# Paciente
class Paciente(models.Model):
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    observacoes = models.TextField(null=True, blank=True)
    criado_em = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return f'{self.nome}'
    

# Atendimento - Representa uma sessão / consulta
class Atendimento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='atendimentos')
    profissional = models.ForeignKey(User, on_delete=models.CASCADE, related_name='atendimentos')
    data_atendimento = models.DateTimeField()
    resumo = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.paciente} - {self.data_atendimento.strftime("%d/%m/%Y")}'