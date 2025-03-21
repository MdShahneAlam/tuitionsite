from django.contrib import admin
from .models import Teachers, StudentsQuery, Feedback

# Register your models here.
admin.site.register(Teachers)
admin.site.register(StudentsQuery)
admin.site.register(Feedback)
