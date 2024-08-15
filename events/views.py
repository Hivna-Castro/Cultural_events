from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Evento
from .forms import EventoForm


def index(request):
    events = Evento.objects.all()
    return render(request, 'events/index.html', {'eventos': events})


def add_event(request):
    if request.method == "POST":
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EventoForm()
    
    return render(request, 'events/add_event.html', {'form': form})

def edit_event(request, evento_id):
    event = get_object_or_404(Evento, id=evento_id)

    if request.method == "POST":
        form = EventoForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EventoForm(instance=event)
    
    return render(request, 'events/edit_event.html', {'form': form})


def delete_event(request, evento_id):
    try:
        event = Evento.objects.get(pk=evento_id)
        event.delete()
    except Evento.DoesNotExist:
        raise Http404("Evento não encontrado")
    return redirect('index')