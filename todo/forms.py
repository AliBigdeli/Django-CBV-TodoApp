from django import forms
from .models import Task

# Reordering Form and View


class TaskUpdateForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control rounded-4",
                "name": "title",
                "placeholder": "enter the title",
            }
        ),
        label="",
    )

    class Meta:
        model = Task
        fields = ("title",)
