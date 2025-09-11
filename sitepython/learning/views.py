from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView, DetailView, CreateView
from .models import Categories, ListExercises, Tasks, AddLesson
from .forms import TaskForm, AddLessonForm
from django.contrib import messages


class LearningHome(TemplateView):
    template_name = 'learning/index.html'
    title_page = 'Главная страница'
    
 
def show_categories(request):
    categories = Categories.objects.all().only('title', 'context')

    return render(request, 'learning/list_post.html', {'categories': categories})


def show_exercises(request, cat_id):
    category = get_object_or_404(Categories, id=cat_id)
    exercises = ListExercises.objects.filter(cat_id=category.pk)

    return render(request, 'learning/exercises.html', {'exercises': exercises, 'category': category})


def show_task(request, listcat_id):
        listcat = get_object_or_404(ListExercises, id=listcat_id)
        
        try:
            task = Tasks.objects.get(listcat=listcat)
        except Tasks.DoesNotExist:
            return HttpResponse("Задача не найдена", status=404)

        form = TaskForm(instance=task)
       
        if request.method == 'POST':
            form = TaskForm(request.POST, example_output=task.example_output)
        if form.is_valid():
            return redirect('happy')
        
        return render(request, 'learning/list_task.html', {'task': task, 'listcat': listcat, 'form': form})


class AddLessonView(LoginRequiredMixin, CreateView):
    form_class = AddLessonForm
    template_name = 'learning/addlesson.html'
    title_page = 'Добавление урока'

    def form_valid(self, form):
        try:
            AddLesson.objects.create(**form.cleaned_data)
        except:
            form.add_error('Упс, gохоже возникла ошибка добавления урока')
    


class Happy(TemplateView):
    template_name = 'learning/happy.html'