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


def pac_list_view(request):
    return render(request, "pacapp/pac_list.html", {
        "active_page": "pac_list"
    })
## placeholder view
def pac_edit_view(request, pk):
    return render(request, "pacapp/pac_form.html", {
        "active_page": "pac_form",
        "mode": "edit",
        "pac": {
            "pk": pk,
            "first_name": "Sarah",
            "last_name": "Mitchell",
            "pac_id": "PAC-8821",
            "email": "s.mitchell@paceacademy.com",
        }
    })

def pac_create_view(request):
    """
    PAC Create page (mock mode)
    - GET: show empty form
    - POST: pretend save + redirect
    """
    if request.method == "POST":
        messages.success(request, "PAC saved (mock mode).")
        return redirect("pac_list")

    return render(request, "pacapp/pac_form.html", {
        "active_page": "pac_form",
        "mode": "create",
        "pac": {
            "pk": None,
            "first_name": "",
            "last_name": "",
            "pac_id": "",
            "email": "",
        }
    })

def pac_edit_view(request, pk):
    """
    PAC Edit page (mock mode)
    - GET: show pre-filled form
    - POST: pretend update + redirect
    """
    mock_pacs = {
        1: {"pk": 1, "first_name": "Sarah", "last_name": "Mitchell", "pac_id": "PAC-8821", "email": "s.mitchell@paceacademy.com"},
        2: {"pk": 2, "first_name": "James", "last_name": "Roberts", "pac_id": "PAC-9102", "email": "j.roberts@paceacademy.com"},
    }

    pac = mock_pacs.get(pk)
    if not pac:
        messages.error(request, "PAC not found (mock mode).")
        return redirect("pac_list")

    if request.method == "POST":
        messages.success(request, f"PAC #{pk} updated (mock mode).")
        return redirect("pac_list")

    return render(request, "pacapp/pac_form.html", {
        "active_page": "pac_form",
        "mode": "edit",
        "pac": pac
    })

def pac_delete_view(request, pk):
    """
    PAC Delete (POST only)
    """
    if request.method == "POST":
        messages.success(request, f"PAC #{pk} deleted (mock mode).")
        return redirect("pac_list")

    return redirect("pac_edit", pk=pk)


def assign_pac_view(request):
    """
    Mock Assign/Change PAC page.

    - GET: show two tables with radio buttons.
    - POST: read selected student + selected pac, then show a success message.
    """

    # Mock students
    students = [
        {
            "pk": 1,
            "student_id": "S0001",
            "first_name": "Jacob",
            "last_name": "White",
            "email": "S0001@paceacademy.com",
            "enrollment_date": "Feb 11, 2026",
        },
        {
            "pk": 2,
            "student_id": "S0002",
            "first_name": "Jade",
            "last_name": "Darton",
            "email": "S0002@paceacademy.com",
            "enrollment_date": "Feb 11, 2026",
        },
    ]

    # Mock PACs
    pacs = [
        {
            "pk": 1,
            "pac_id": "PAC-8821",
            "first_name": "Pac",
            "last_name": "Man",
            "email": "pacman@paceacademy.com",
            "specialisation": "Software",
        },
        {
            "pk": 2,
            "pac_id": "PAC-8822",
            "first_name": "Pac",
            "last_name": "Lady",
            "email": "paclady@paceacademy.com",
            "specialisation": "Childcare",
        },
    ]

    # Defaults for which radio buttons appear selected
    selected_student = None
    selected_pac = None

    if request.method == "POST":
        # Grab the selected IDs from the submitted form
        selected_student = request.POST.get("selected_student")
        selected_pac = request.POST.get("selected_pac")

        # Basic validation
        if not selected_student or not selected_pac:
            messages.error(request, "Please select both a student and a PAC before confirming.")
            return redirect("assign_pac")

        # Look up the chosen student + pac in mock list
        student_obj = next((s for s in students if str(s["pk"]) == str(selected_student)), None)
        pac_obj = next((p for p in pacs if str(p["pk"]) == str(selected_pac)), None)

        if not student_obj or not pac_obj:
            messages.error(request, "Selection not found (mock mode).")
            return redirect("assign_pac")


        # student.assigned_pac = pac
        # student.save()
        messages.success(
            request,
            f"Assigned {student_obj['first_name']} {student_obj['last_name']} to {pac_obj['pac_id']}."
        )

        # Keep the radios selected after submission
        selected_student = int(student_obj["pk"])
        selected_pac = int(pac_obj["pk"])

    return render(request, "pacapp/assign_pac.html", {
        "active_page": "assign_pac",
        "students": students,
        "pacs": pacs,
        "selected_student": selected_student,
        "selected_pac": selected_pac,
    })
    return render(request, "pacapp/student_list.html")
