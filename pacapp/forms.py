from django import forms
from .models import Students

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = [
            "first_name",
            "last_name",
            "student_id",
            "email",
            "enrollment_date",
            "assigned_pac",
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "sf-input"}),
            "last_name": forms.TextInput(attrs={"class": "sf-input"}),
            "student_id": forms.TextInput(attrs={"class": "sf-input"}),
            "email": forms.EmailInput(attrs={"class": "sf-input"}),
            "enrollment_date": forms.DateInput(
                attrs={"class": "sf-input", "type": "date"}
            ),
            "assigned_pac": forms.Select(attrs={"class": "sf-input"}),
        }