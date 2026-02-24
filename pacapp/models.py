from django.db import models


# Create your models here.


class Pacs(models.Model):
    pac_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} {str(self.pac_id)}'

class Students(models.Model):
    student_id = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    enrollment_date = models.DateField()
    assigned_pac = models.ForeignKey(Pacs, on_delete=models.CASCADE, related_name='students', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.student_id}'
