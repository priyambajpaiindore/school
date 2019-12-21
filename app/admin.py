from django.contrib import admin

# Register your models here.
from .models import (School,
                    Student,
                    Teacher,
                    User
)

admin.site.register(School)
admin.site.register(Student)
admin.site.register(User)
admin.site.register(Teacher)