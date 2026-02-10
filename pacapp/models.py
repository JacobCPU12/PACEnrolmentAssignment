from django.db import models

# Create your models here.
class PersonalAcademicCoach(models.Model):
    first_name = models.CharField(max_length=100),
    last_name = models.CharField(max_length=100),
    email = models.EmailField(),
    office_id = models.IntegerField(),
    specialization_id = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    office_id = models.IntegerField()
    enrolment_date = models.DateField()
    assigned_pac_id = models.IntegerField()
    def __str__(self):
        return f'{self.first_name} {self.last_name}'