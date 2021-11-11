from django.contrib import admin
from student.models import studyMaterial, result, notice
# Register your models here.
admin.site.register(studyMaterial)

admin.site.register(result)

admin.site.register(notice)

