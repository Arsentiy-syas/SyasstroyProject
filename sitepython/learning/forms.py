from django import forms
from django.shortcuts import redirect
from django.core.exceptions import ValidationError
from .models import Tasks

class TaskForm(forms.ModelForm):
    text_input = forms.CharField(label='Пишите код здась', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        self.example_output = kwargs.pop('example_output', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = Tasks
        fields = ['text_input']

    def clean_text_input(self):
        text_input = self.cleaned_data.get('text_input')

        if text_input != self.example_output:
            raise ValidationError('Подумай еще')

        return text_input 
