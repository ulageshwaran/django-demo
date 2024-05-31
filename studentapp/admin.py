from django.contrib import admin
from .models import student,Profile,course

# Register your models here.
admin.site.register(student)
admin.site.register(course)
admin.site.register(Profile)