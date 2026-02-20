from django.urls import path
from . import views

urlpatterns = [

    # Auth
    path("", views.login_view, name="login"),
    path("home/", views.home_view, name="home"),
    path("logout/", views.logout_view, name="logout"),

    # Students
    path("student_form/", views.student_create_view, name="student_form"),   # create
    path("student_list/", views.student_list_view, name="student_list"),
    path("student/<int:pk>/edit/", views.student_edit_view, name="student_edit"),
    path("student/<int:pk>/delete/", views.student_delete_view, name="student_delete"),

    # PACs
    path("pac_form/", views.pac_create_view, name="pac_form"),               # create
    path("pac_list/", views.pac_list_view, name="pac_list"),
    path("pac/<int:pk>/edit/", views.pac_edit_view, name="pac_edit"),
    path("pac/<int:pk>/delete/", views.pac_delete_view, name="pac_delete"),

    # Assign PAC
    path("assign_pac/", views.assign_pac_view, name="assign_pac"),
]
