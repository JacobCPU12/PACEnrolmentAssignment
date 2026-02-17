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
    """
    Handles editing an existing student.

    - GET request → Display the form pre-filled with student data.
    - POST request → Pretend to update student (mock mode) and redirect.
    """

    # Mock student data (not using database yet)
    mock_students = {
        1: {
            "pk": 1,
            "first_name": "Jacob",
            "last_name": "White",
            "student_id": "S0001",
            "email": "S0001@paceacademy.com",
            "enrollment_date": "2026-02-11",
        },
        2: {
            "pk": 2,
            "first_name": "Jade",
            "last_name": "Darton",
            "student_id": "S0002",
            "email": "S0002@paceacademy.com",
            "enrollment_date": "2026-02-11",
        },
    }

    # Try to find the student by primary key (pk)
    student = mock_students.get(pk)

    # If student not found, redirect back to student list
    if not student:
        messages.error(request, "Student not found (mock mode).")
        return redirect("student_list")

    # If the form was submitted (POST request),
    # this simulates saving changes to the database
    if request.method == "POST":
        # In real implementation:
        # - Validate form
        # - Save updated student to DB
        messages.success(request, f"Student #{pk} updated (mock mode).")

        # After updating, redirect back to the student list page
        return redirect("student_list")

    # If it's a GET request, render the form in edit mode
    return render(request, "pacapp/student_form.html", {
        "active_page": "student_form",
        "mode": "edit",
        "student": student,
    })

@login_required
def student_delete_view(request, pk):
    """
    Handles deleting a student.

    - Only allows deletion via POST request.
    - Prevents accidental deletes via URL (GET request).
    """

    # Only allow delete if the request method is POST
    if request.method == "POST":

        # In real implementation:
        # - Fetch student by pk
        # - Call student.delete()
        messages.success(request, f"Student #{pk} deleted (mock mode).")

        # After deleting, redirect back to the list page
        return redirect("student_list")

    # If someone tries to access delete via browser URL,
    # redirect them back to the edit page instead
    return redirect("student_edit", pk=pk)
