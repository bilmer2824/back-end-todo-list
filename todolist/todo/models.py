from django.db import models
from django import *
# Create your models here.


class Todos(models.Model):
    todo_title = models.TextField(max_length=50, verbose_name="Название", null=True, blank=True)
    todo_data_created = models.DateTimeField(auto_now=True, verbose_name="созданные данные")
    todo_data_updated = models.DateTimeField(auto_now_add=True)
    todo_text = models.TextField(max_length=250, verbose_name="Содержание", null=True, blank=True)
    todo_published = models.BooleanField(default=True, verbose_name="опубликован")

    def __str__(self):
        return self.todo_title

    class Meta:
        verbose_name = "список дело"
        verbose_name_plural = "список делов"
