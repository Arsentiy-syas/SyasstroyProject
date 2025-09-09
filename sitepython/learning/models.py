from django.db import models
from django.urls import reverse

class Categories(models.Model):
    title = models.CharField(max_length=100, blank=False, verbose_name='Категории')
    context = models.TextField(max_length=255, blank=False, verbose_name='Описание')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='slug')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'cat_id': self.slug})


class ListExercises(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название уроков')
    content = models.CharField(max_length=255, verbose_name='Описание уроков')
    cat = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='exercises')

    def __str__(self):
        return self.title
    

class Tasks(models.Model):
    task = models.CharField(verbose_name='Задания')
    example_output = models.CharField(verbose_name='Пример выхода')
    listcat = models.ForeignKey(ListExercises, on_delete=models.CASCADE, null=True, related_name='listtask')

    







    
