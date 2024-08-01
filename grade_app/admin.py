from django.contrib import admin
from grade_app import models

# Register your models here.

admin.site.register(models.User_model)
admin.site.register(models.Student)
admin.site.register(models.Course)
admin.site.register(models.Grade)