from django import forms
from django.core.exceptions import ValidationError

from .models import ToDo


class ToDoForm(forms.ModelForm):
    completed = forms.BooleanField(required=False)

    class Meta:
        model = ToDo
        fields = ['id', 'name', 'description', 'user',  'completed']

    def clean_name(self):
        if not self.cleaned_data.get('name') and self.instance.name:
            return self.instance.name

        if len(self.cleaned_data.get('name')) < 2:
            raise ValidationError('Value must be more than 1 character.')

        return self.cleaned_data.get('name')


class ToDoUpdateForm(ToDoForm):
    completed = forms.BooleanField(required=False)

    class Meta:
        model = ToDo
        fields = ['name', 'description', 'user', 'completed']

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['name'] = cleaned_data.get('name') or self.instance.name
        cleaned_data['description'] = cleaned_data.get('description') or self.instance.description
        cleaned_data['user'] = cleaned_data.get('user') or self.instance.user
        cleaned_data['completed'] = cleaned_data.get('completed') if cleaned_data.get('completed') is not None else self.instance.completed

    def clean_name(self):
        return self.cleaned_data.get('name').strip() if self.cleaned_data.get('name') else None


class ToDoFilterForm(forms.Form):
    name = forms.CharField(required=False)