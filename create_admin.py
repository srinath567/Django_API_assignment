import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

try:
    user = User.objects.create_user(
        username='admin',
        email='admin@example.com',
        password='admin123',
        is_staff=True,
        is_superuser=True
    )
    print('Admin user created successfully!')
    print('Username: admin')
    print('Password: admin123')
except Exception as e:
    print(f'Error creating admin user: {str(e)}') 