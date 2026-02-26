from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import Students
from .models import Pacs
from .forms import StudentForm
from .forms import PacForm

# Login page
def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    # once submitted
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        messages.error(request, "Invalid username or password.")

    return render(request, "pacapp/login.html")

# home page
def home_view(request):
    student=Students.objects.all()
    context={
        'students':student,
        'active_page': 'dashboard',
    }
    return render(request, "pacapp/home.html", context)

def logout_view(request):
    logout(request)
    return redirect("login")


def student_list_view(request):
    student=Students.objects.all()
    context={
        'students':student,
        'active_page': 'student_list',
    }
    return render(request, "pacapp/student_list.html", context)


def pac_list_view(request):
    pacs=Pacs.objects.all()
    print("PAC COUNT:", pacs.count())
    context= {
        'pacs':pacs,
        'active_page': 'pac_list',
    }
    return render(request, "pacapp/pac_list.html", context)

# used for managing pacs
def pac_form_view(request):
    return render(request, "pacapp/pac_form.html", {"active_page": "pac_form"})

# used for creating students
def student_create_view(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student created successfully.")
            return redirect("student_list")
    else:
        form = StudentForm()

    return render(request, "pacapp/student_form.html", {
        "active_page": "student_form",
        "mode": "create",
        "form": form,
    })

# editing students
def student_edit_view(request, pk):
    student = get_object_or_404(Students, pk=pk)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully.")
            return redirect("student_list")
    else:
        form = StudentForm(instance=student)

    return render(request, "pacapp/student_form.html", {
        "active_page": "student_form",
        "mode": "edit",
        "form": form,
        "student": student,
    })


def student_delete_view(request, pk):
    """
    Handles deleting a student.

    - Only allows deletion via POST request.
    - Prevents accidental deletes via URL (GET request).
    """
    student = get_object_or_404(Students, pk=pk)

    # Only allow delete if the request method is POST
    if request.method == "POST":

        # In real implementation:
        # - Fetch student by pk
        student.delete()
        messages.success(request, f"Student #{pk} deleted (mock mode).")

        # After deleting, redirect back to the list page
        return redirect("student_list")

    # If someone tries to access delete via browser URL,
    # redirect them back to the edit page instead
    return redirect("student_edit", pk=pk)

def pac_create_view(request):
    if request.method == "POST":
        form = PacForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "PAC created successfully.")
            return redirect("pac_list")
    else:
        form = PacForm()

    return render(request, "pacapp/pac_form.html", {
        "active_page": "pac_form",
        "mode": "create",
        "form": form,
    })

# editing a pac
def pac_edit_view(request, pk):
    pac = get_object_or_404(Pacs, pk=pk)

    if request.method == "POST":
        form = PacForm(request.POST, instance=pac)
        if form.is_valid():
            form.save()
            messages.success(request, "PAC updated successfully.")
            return redirect("pac_list")
    else:
        form = PacForm(instance=pac)

    return render(request, "pacapp/pac_form.html", {
        "active_page": "pac_form",
        "mode": "edit",
        "form": form,
        "pac": pac,
    })

# deleting a pac
def pac_delete_view(request, pk):
    pac = get_object_or_404(Pacs, pk=pk)

    if request.method == "POST":
        pac.delete()
        messages.success(request, "PAC deleted successfully.")
        return redirect("pac_list")

    return redirect("pac_edit", pk=pk)


def assign_pac_view(request):
    """
    Assign / Change PAC page using real models.
    """
    students = Students.objects.all().order_by('student_id')
    pacs = Pacs.objects.all().order_by('pac_id')  # Replace with your actual PAC model

    selected_student = None
    selected_pac = None

    if request.method == "POST":
        selected_student = request.POST.get("selected_student")
        selected_pac = request.POST.get("selected_pac")

        if not selected_student or not selected_pac:
            messages.error(request, "Please select both a student and a PAC before confirming.")
        else:
            student_obj = get_object_or_404(Students, pk=selected_student)
            pac_obj = get_object_or_404(Pacs, pk=selected_pac)

            student_obj.assigned_pac = pac_obj
            student_obj.save()

            messages.success(
                request,
                f"Assigned {student_obj.first_name} {student_obj.last_name} to {pac_obj.first_name} {pac_obj.last_name}."
            )

            # Keep radio buttons selected
            selected_student = student_obj.pk
            selected_pac = pac_obj.pk

    return render(request, "pacapp/assign_pac.html", {
        "active_page": "assign_pac",
        "students": students,
        "pacs": pacs,
        "selected_student": selected_student,
        "selected_pac": selected_pac,
    })
