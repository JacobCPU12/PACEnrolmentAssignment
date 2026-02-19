from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("home/", views.home_view, name="home"),
    path("logout/", views.logout_view, name="logout"),

    # sidebar links
    path("student_list/", views.student_list_view, name="student_list"),
    path("student_form/", views.student_form_view, name="student_form"),
    path("assign_pac/", views.assign_pac_view, name="assign_pac"),
    path("pac_list/", views.pac_list_view, name="pac_list"),
    path("pac_form/", views.pac_form_view, name="pac_form"),


# Students CRUD
    path("student_form/", views.student_create_view, name="student_form"),               # student create
    path("student/<int:pk>/edit/", views.student_edit_view, name="student_edit"),       # student edit
    path("student/<int:pk>/delete/", views.student_delete_view, name="student_delete"), # student delete

    path("pac_list/", views.pac_list_view, name="pac_list"),
    path("pac/<int:pk>/edit/", views.pac_edit_view, name="pac_edit"),

# PACs CRUD
    path("pac_form/", views.pac_create_view, name="pac_form"),               # PAC create
    path("pac/<int:pk>/edit/", views.pac_edit_view, name="pac_edit"),        # PAC edit
    path("pac/<int:pk>/delete/", views.pac_delete_view, name="pac_delete"),  # PAC delete


    path("assign_pac/", views.assign_pac_view, name="assign_pac"),

    ]