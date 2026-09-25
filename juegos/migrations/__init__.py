{% extends 'juegos/base.html' %}

{% block title %}{{ game.title }}{% endblock %}

{% block content %}
  <div class="card" style="max-width: 900px; margin: 40px auto 0;">
    <h2>{{ game.title }}</h2>
    <p><strong>Género:</strong> {{ game.genre }}</p>
    <p><strong>Año:</strong> {{ game.release_year }}</p>
    <p><strong>Desarrollador:</strong> {{ game.developer }}</p>
    <p><strong>Descripción:</strong> {{ game.description }}</p>

    {% if delete_mode %}
      <form method="post">
        {% csrf_token %}
        <p>¿Estás seguro de que deseas eliminar este juego?</p>
        <div class="btn-row" style="justify-content:flex-start; margin-top:24px;">
          <button type="submit" class="btn btn-danger">Sí, eliminar</button>
          <a href="{% url 'home' %}" class="btn btn-secondary">Cancelar</a>
        </div>
      </form>
    {% else %}
      <div class="btn-row" style="justify-content:flex-start; margin-top:24px;">
        <a href="{% url 'game_update' game.pk %}" class="btn btn-primary">Editar</a>
        <a href="{% url 'game_delete' game.pk %}" class="btn btn-danger">Eliminar</a>
        <a href="{% url 'home' %}" class="btn btn-secondary">Volver</a>
      </div>
    {% endif %}
  </div>
{% endblock %}
