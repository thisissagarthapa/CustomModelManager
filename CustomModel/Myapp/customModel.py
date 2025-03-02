from django.db import models

class CustomModel(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('name')


class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('name').filter(age__gte=22)  # Default ordering by name  and age must be greater than or equal to 22
    
    def get_stu_age_range(self,a1,a2):
        return self.get_queryset().filter(age__range=(a1,a2)) #filter by range of age
