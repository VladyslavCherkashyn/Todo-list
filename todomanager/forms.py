from django import forms
from .models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
        widgets = {"deadline": forms.DateTimeInput(attrs={"type": "datetime-local"})}


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["is_completed"]


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
