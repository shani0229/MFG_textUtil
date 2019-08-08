from django.db import models

# Create your models here.

class emp(models.Model):
    emp_name = models.CharField(max_length=10)
    emp_father = models.CharField(max_length=10)
    emp_Email = models.EmailField(max_length=30)
    emp_Id = models.IntegerField()


def __str__(self):
    return self.emp_name    




