# Pagina de Juegos PS2

Proyecto web de Django para administrar una colección de juegos de PlayStation 2 con autenticación segura.

## Requisitos

- Python 3.11+
- pip

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Credenciales de acceso

- Usuario: `ivan`
- Contraseña: `inacap2026`

## Funcionalidades

- Login con sesión segura
- Listado de juegos de PS2
- Crear, editar, eliminar y ver detalles de cada juego
- CRUD protegido con autenticación
- Panel de administración de Django

## Acceso

Abrir en el navegador:

```text
http://127.0.0.1:8000/
```
