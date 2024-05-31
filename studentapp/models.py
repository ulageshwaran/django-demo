from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class course(models.Model):
    course_id = models.IntegerField()
    course_name = models.CharField(max_length=100)
    course_fee = models.IntegerField()

    def __str__(self):
        return f' {self.course_id}'

class student(models.Model):
    student_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    feild_of_study = models.CharField(max_length=100)
    course_id = models.ForeignKey(course, on_delete = models.CASCADE)
    Fees_status = models.IntegerField()

    def __str__(self):
        return f'student {self.first_name} {self.last_name}'

class Profile(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f' {self.username}'
