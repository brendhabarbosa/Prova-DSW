from django.db import models

# Create your models here.

class Modalidade(models.Model):
    MODALIDADE = {
        "C": "Coletiva",
        "I": "Individual",
    }
    nome = models.CharField(max_length=100, unique=True)
    tipo = models.CharField(max_length=1, choices = MODALIDADE)
    max_atletas = models.PositiveIntegerField()
    class Meta:
        ordering = ['nome']
        verbose_name = 'modalidades'
        verbose_name_plural = 'modalidades'
    def __str__(self):
        return self.nome

class Atleta(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=100, unique=True)
    data_nascimento = models.DateField()
    modalidade = models.ManyToManyField(Modalidade, related_name="atletas")
    class Meta:
        ordering = ['nome']
        verbose_name = 'atleta'
        verbose_name_plural = 'atletas'
    def __str__(self):
        return self.nome

class Tecnico(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=100)
    class Meta:
        ordering = ['nome']
        verbose_name = 'técnico'
        verbose_name_plural = 'técnicos'
    def __str__(self):
        return self.nome

class Equipe(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    curso = models.CharField(max_length=100)
    cor = models.CharField(max_length=100)
    criada_em = models.DateTimeField(auto_now_add=True)
    atleta = models.ForeignKey(Atleta,on_delete = models.PROTECT, related_name="equipes", null=True, blank =True)
    tecnico = models.OneToOneField(Tecnico, on_delete = models.CASCADE, related_name="equipes", null=True, blank=True)
    class Meta:
        ordering = ['nome']
        verbose_name = 'equipe'
        verbose_name_plural = 'equipes'
    def __str__(self):
        return self.nome

