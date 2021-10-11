from django.db import models


class EmployeeModel(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    user_phno = models.IntegerField()
    user_email = models.EmailField()
    user_pass = models.CharField(max_length=50)
