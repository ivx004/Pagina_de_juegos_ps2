from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Game
from .forms import GameForm


@login_required(login_url='login')
def game_list(request):
    games = Game.objects.all().order_by('title')
    return render(request, 'juegos/game_list.html', {'games': games})


@login_required(login_url='login')
def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'juegos/game_detail.html', {'game': game})


@login_required(login_url='login')
def game_create(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Juego creado correctamente.')
            return redirect('home')
    else:
        form = GameForm()
    return render(request, 'juegos/game_form.html', {'form': form, 'title': 'Crear juego'})


@login_required(login_url='login')
def game_update(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            messages.success(request, 'Juego actualizado correctamente.')
            return redirect('home')
    else:
        form = GameForm(instance=game)
    return render(request, 'juegos/game_form.html', {'form': form, 'title': 'Editar juego'})


@login_required(login_url='login')
def game_delete(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        game.delete()
        messages.success(request, 'Juego eliminado correctamente.')
        return redirect('home')
    return render(request, 'juegos/game_detail.html', {'game': game, 'delete_mode': True})
