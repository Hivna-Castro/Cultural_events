from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'

        labels = {
            'titulo': 'Titulo*',
            'data_inicio': 'Data Inicio*',
            'local': 'Local*',
            'cidade': 'Cidade*',
            'horario': 'Horário*',
            'tipo': 'Tipo*',
        }

        required = {
            'titulo': True,
            'data_inicio': True,
            'local': True,
            'cidade': True,
            'horario': True,
            'tipo': True,
        }
  
    


