from django.db import models

# Create your models here.
class Evento(models.Model):
    TITLE_CHOICES = [
        ('show', 'Show'),
        ('teatro', 'Apresentação Teatral'),
        ('orquestra', 'Orquestra'),
        ('musical', 'Musical'),
        ('humor', 'Show de Humor'),
        ('magica', 'Mágica'),
        ('arte', 'Arte'),
        ('tecnologia', 'Tecnologia'),
        ('gastronomia', 'Gastronomia'),
        ('esporte', 'Esporte'),  
        ('cinema', 'Cinema'),
        ('workshop', 'Workshop')
    ]

    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50, choices=TITLE_CHOICES)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    gratuito = models.BooleanField(default=False)
    local = models.CharField(max_length=200)
    horario = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    quantidade_vagas = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.titulo