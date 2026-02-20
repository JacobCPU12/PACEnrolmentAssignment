from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("home/", views.home_view, name="home"),
    path("logout/", views.logout_view, name="logout"),

    # sidebar links
    path("student_list/", views.student_list_view, name="student_list"),
    path("student/create/", views.student_create_view, name="student_create"),
    path("assign_pac/", views.assign_pac_view, name="assign_pac"),
    path("pac_list/", views.pac_list_view, name="pac_list"),
    path("pac/create/", views.pac_create_view, name="pac_create"),


    # Students CRUD
    # only edit and delete - since create is already defined in the sidebar
    path("student/<int:pk>/edit/", views.student_edit_view, name="student_edit"),
    path("student/<int:pk>/delete/", views.student_delete_view, name="student_delete"),

    # PACs CRUD
    # only edit and delete - since create and assign is already defined in the sidebar
    path("pac/<int:pk>/edit/", views.pac_edit_view, name="pac_edit"),
    path("pac/<int:pk>/delete/", views.pac_delete_view, name="pac_delete"),

    ]