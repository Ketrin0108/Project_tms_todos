from django.contrib.auth.models import User

from .models import ToDo


def create_initial_db():
    user_1 = User.objects.create_user(
        username='PopCrave',
        email='pop.crave@gmail.com',
        password='3456',
        is_active=True
    )
    user_2 = User.objects.create_user(
        username='SaeedDiCaprio',
        email='SaeedDiCaprio@gmail.com',
        password='12345',
        is_active=True
    )
    user_3 = User.objects.create_user(
        username='PopCulture2000s',
        email='PopCulture2000s@gmail.com',
        password='78945',
        is_active=True
    )

    ToDo(
        name='go to the store',
        description='out of products',
        user=user_2
    ).save()
    ToDo(
        name='buy flowers',
        description='mothers birthday',
        user=user_1
    ).save()
    ToDo(
        name='clean up the house',
        description='the apartment is dirty',
        user=user_3
    ).save()


