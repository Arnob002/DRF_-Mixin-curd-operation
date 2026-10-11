from django.db import models

# Create your models here.
class employeeModel(models.Model):
    emp_id = models.CharField(max_length=20,null=True)
    emp_name = models.CharField(max_length=20,null=True)
    designation = models.CharField(null=True)

    def __str__(self):
        return f'{self.emp_name}'