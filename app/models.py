from django.db import models

# Create your models here.
class test(models.Model):
    student_name = models.CharField(max_length=100)
    username = models.CharField(max_length=122)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=12 )
    password = models.CharField(max_length=20)