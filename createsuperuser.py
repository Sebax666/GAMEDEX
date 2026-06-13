import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GAMEDEX.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="Sebax666").exists():
    User.objects.create_superuser(
        username="Sebax666",
        email="sebax666@gmail.com",
        password="sebax666"
    )
    print("Superusuario creado")
else:
    print("El superusuario ya existe")