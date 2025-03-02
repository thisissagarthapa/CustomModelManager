from django.db import models
from .customModel import CustomModel,CustomManager

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField(unique=True)
    students=CustomModel()  #custom model manager
    stu=CustomManager() #nextCustommodel manager
    objects=models.Manager() #default manager

    def __str__(self):
        return self.name

class ProxyStudents(Student):
    student_1=CustomManager()
    class Meta:
        proxy=True
        # ordering=["id"]