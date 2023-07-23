from time import sleep
from celery import shared_task
from tms.celery import app
from datetime import datetime
from django.contrib.auth.models import User
import logging
from .models import ToDo
from celery import shared_task

logger = logging.getLogger(__name__)

@shared_task()
def logging_task(params=None):
    print(params)
    sleep(10)

# Задача для логгирования завершенных задач для каждого пользователя
@app.task
def log_completed_tasks():
    from todos.models import ToDo

    today = datetime.now().date()

    # Получение все завершенные задачи за сегодня длякаждого пользователя
    users = User.objects.all()

    # Логгирование завершенных задач для каждого пользователя
    for user in users:
        # Получение завершенных задач для данного пользователя сегодня
        completed_tasks = ToDo.objects.filter(user=user, completed=True, updated__date=today)

        # Логгирование завершенных задач в файл
        file_name = f"user_{user.id}_{today}.txt"
        with open(file_name, 'a') as file:
            for task in completed_tasks:
                file.write(f"Task ID:{task.id}, Name:{task.name}, Updated At: {task.updated}\n")

        # Логгирование завершенных задач в файл
        logger.info(f"Completed tasks for user {user.id}:")

    return 'Task logging completed.'