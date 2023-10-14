from django import forms
from .models import Todos

class TodosForm(forms.ModelForm):
    class Meta:
        model = Todos
        fields = ['todo_title', 'todo_text']
        widgets = {
            'todo_title': forms.TextInput(attrs={
                'class': 'windows-form-label-input',
                'name': 'title',
                'type': 'text',
                'placeholder': 'Название'
            }),
            'todo_text': forms.TextInput(attrs={
                'class': 'windows-form-label-input',
                'name': 'text',
                'type': 'text',
                'placeholder': 'Содержание'
            })
        }



