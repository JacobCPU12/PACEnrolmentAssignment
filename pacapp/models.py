from django.db import models


# Create your models here.


class Pacs(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Students(models.Model):
    student_id = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    enrollment_date = models.DateField(auto_now_add=True)
    assigned_pac = models.ForeignKey(Pacs, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.student_id}'


class PastoralNotes(models.Model):
    note = models.TextField()
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    pac = models.ForeignKey(Pacs, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Note for{self.student_id}'
