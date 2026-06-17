from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .forms import RegisterForm, LoginForm


def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = CustomUser.create(
                email=data["email"],
                password=data["password"],
                first_name=data["first_name"],
                last_name=data["last_name"],
                middle_name=data["middle_name"],
            )
            if user is not None:
                user.update(role=data["role"])
                login(
                    request,
                    user,
                    backend="django.contrib.auth.backends.ModelBackend",
                )
                return redirect("user_list")
            form.add_error(None, "Не вдалося створити користувача")
    else:
        form = RegisterForm()

    return render(request, "authentication/register.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect("user_list")
            form.add_error(None, "Невірний email або пароль")
    else:
        form = LoginForm()

    return render(request, "authentication/login.html", {"form": form})


@login_required
def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect("login_user")

    return redirect("user_list")


@login_required
def user_list(request):
    # Перевірка чи роль == 1 (librarian)
    if request.user.role != 1:
        return redirect("book_list")

    users = CustomUser.get_all()
    return render(request, "authentication/user_list.html", {"users": users})


@login_required
def user_detail(request, user_id):
    if request.user.role != 1:
        return render(request, "authentication/access_denied.html")

    target_user = CustomUser.get_by_id(user_id)
    if not target_user:
        return redirect("user_list")

    return render(
        request, "authentication/user_detail.html", {"target_user": target_user}
    )
