from django import forms

from .models import CustomUser, ROLE_CHOICES


class RegisterForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        max_length=100,
        widget=forms.EmailInput(attrs={"class": "form-input"}),
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "form-input"}),
    )
    first_name = forms.CharField(
        label="Ім'я",
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-input"}),
    )
    last_name = forms.CharField(
        label="Прізвище",
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-input"}),
    )
    middle_name = forms.CharField(
        label="По батькові",
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-input"}),
    )
    role = forms.TypedChoiceField(
        label="Оберіть вашу роль",
        choices=ROLE_CHOICES,
        coerce=int,
        initial=0,
        widget=forms.RadioSelect,
    )

    def clean_email(self):
        email = self.cleaned_data["email"]
        if CustomUser.get_by_email(email) is not None:
            raise forms.ValidationError("Користувач з таким email вже існує")
        return email


class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"class": "form-input"}),
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "form-input"}),
    )
