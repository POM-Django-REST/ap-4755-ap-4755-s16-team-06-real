from django import forms

from .models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "surname", "patronymic"]
        labels = {
            "name": "Ім'я",
            "surname": "Прізвище",
            "patronymic": "По батькові",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-input"}),
            "surname": forms.TextInput(attrs={"class": "form-input"}),
            "patronymic": forms.TextInput(attrs={"class": "form-input"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["patronymic"].required = False
