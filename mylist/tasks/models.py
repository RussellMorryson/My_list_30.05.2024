from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):    
    title = models.CharField(max_length=255)                    # Название задачи
    description = models.TextField(max_length=255)              # Описание
    term = models.CharField(max_length=10)                      # Срок выполнения
    tag = models.CharField(max_length=20)                       # Тэг
    status = models.CharField(max_length=255)                   # Статус задания
    create_date = models.DateField()                            # Дата создания
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Автор

   
class Tag(models.Model):
    tag = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.tag}'