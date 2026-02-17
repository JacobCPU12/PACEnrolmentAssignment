from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        messages.error(request, "Invalid username or password.")

    return render(request, "pacapp/login.html")


def home_view(request):
    return render(request, "pacapp/home.html", {"active_page": "dashboard"})

def logout_view(request):
    logout(request)
    return redirect("login")


def student_list_view(request):
    return render(request, "pacapp/student_list.html", {"active_page": "student_list"})


def student_form_view(request):
    return render(request, "pacapp/student_form.html", {"active_page": "student_form"})


def assign_pac_view(request):
    return render(request, "pacapp/assign_pac.html", {"active_page": "assign_pac"})


def pac_list_view(request):
    return render(request, "pacapp/pac_list.html", {"active_page": "pac_list"})


def pac_form_view(request):
    return render(request, "pacapp/pac_form.html", {"active_page": "pac_form"})


def student_create_view(request):
    # No real saving yet, just render the form in "create" mode.
    context = {
        "active_page": "student_form",
        "mode": "create",
        "student": {
            "first_name": "",
            "last_name": "",
            "student_id": "",
            "email": "",
            "enrollment_date": "",
        },
    }
    return render(request, "pacapp/student_form.html", context)

def student_edit_view(request, pk):
    # Mock existing student (fetch from DB later)
    context = {
        "active_page": "student_form",
        "mode": "edit",
        "student": {
            "pk": pk,
            "first_name": "Jade",
            "last_name": "Darton",
            "student_id": "S0002",
            "email": "S0002@paceacademy.com",
            "enrollment_date": "2026-02-11",
        },
    }
    return render(request, "pacapp/student_form.html", context)

def student_delete_view(request, pk):
    # For now just redirect back to student list
    if request.method == "POST":
        return redirect("student_list")

    # redirect to student list page
    return redirect("student_list")