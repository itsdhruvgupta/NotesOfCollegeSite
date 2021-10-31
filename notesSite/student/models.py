from django.db import models

# Create your models here.

class studyMaterial(models.Model):
    material_title = models.CharField(max_length=200)
    material_detail = models.CharField(max_length=500)
    uploaded_time = models.CharField(max_length=50)
    uploaded_by = models.CharField(max_length=50)
    uploader_course = models.CharField(max_length=100)
    uploader_sem = models.CharField(max_length=20)
    uploader_file = models.FileField(upload_to="static/",default="")