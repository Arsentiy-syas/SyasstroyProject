from django.urls import path
from . import views

urlpatterns = [
    path('', views.LearningHome.as_view(), name='home'),
    path('lessons/', views.show_categories, name='lessons'),
    path('post/<int:cat_id>/', views.show_exercises, name='post'),
    path('task/<int:listcat_id>/', views.show_task, name='task_detail'),
    path('happy/', views.Happy.as_view(), name='happy'),
]