from django.db import models

# Create your models here.

from django.db import models
from django.db import models

from django.db import models


# Create your models here.
# class Bank(models.Model):
#     name = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.name
class District(models.Model):
    name = models.CharField(max_length=30)


class Branch(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     birthdate = models.DateField(null=True, blank=True)
#     college = models.ForeignKey(College, on_delete=models.SET_NULL, null=True)
#     branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
#
#     def __str__(self):
#         return self