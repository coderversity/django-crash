from django import forms
from .models import TodoItem

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['title', 'description', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter title...'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter description...', 'rows': 6}),
            'completed': forms.CheckboxInput(),
        }