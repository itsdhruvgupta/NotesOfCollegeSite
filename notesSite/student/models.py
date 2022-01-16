from django.db import models

# Create your models here.

class studyMaterial(models.Model):
    material_title = models.CharField(max_length=100)
    material_detail = models.CharField(max_length=300)
    uploaded_time = models.CharField(max_length=50)
    uploaded_by = models.CharField(max_length=50)
    uploader_course = models.CharField(max_length=100)
    uploader_sem = models.CharField(max_length=20)
    upload_file = models.FileField(upload_to="static/",default="")

class result(models.Model):
    result_title = models.CharField(max_length=100)
    result_detail = models.CharField(max_length=300)
    uploaded_time = models.CharField(max_length=50)
    uploaded_by = models.CharField(max_length=50)
    result_course = models.CharField(max_length=100)
    result_sem = models.CharField(max_length=20)
    result_batch = models.CharField(max_length=20)
    result_file = models.FileField(upload_to="static/",default="")


class notice(models.Model):
    notice_title = models.CharField(max_length=100)
    result_detail = models.CharField(max_length=200)
    uploaded_time = models.CharField(max_length=50)
    related_dep = models.CharField(max_length=100)

class post_data(models.Model):
    username = models.CharField(max_length=100)
    userprofile = models.ImageField()
    uploaded_time = models.CharField(max_length=100)
    post = models.CharField(max_length=200)
    likes = models.IntegerField()
    desc   = models.CharField(max_length= 1000)
    comments = models.CharField(max_length=100) 