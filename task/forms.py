from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from task.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'],
    )

    class Meta:
        model = Task
        exclude = ("is_completed", )

    def clean_deadline(self):
        deadline = self.cleaned_data.get("deadline")

        if timezone.now() >= deadline:
            raise ValidationError("Invalid date for deadline")
        return deadline
