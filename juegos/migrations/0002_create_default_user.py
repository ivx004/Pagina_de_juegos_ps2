from django.db import migrations


def create_default_user(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    if not User.objects.filter(username='ivan').exists():
        user = User(username='ivan', is_staff=True, is_superuser=True)
        user.set_password('inacap2026')
        user.save()


def reverse_default_user(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    User.objects.filter(username='ivan').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('juegos', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_user, reverse_default_user),
    ]
