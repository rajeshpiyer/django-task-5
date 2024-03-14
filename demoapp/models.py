from django.db import models

class Company(models.Model):
    name = models.CharField(max_length =225)
    location = models.CharField(max_length = 125)
    employee_count = models.IntegerField(default = 0)
    office_count = models.IntegerField(default=0)
    turnover = models.IntegerField(default = 0)

class Employee(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length = 225)
    age = models.IntegerField(default = 18)
    house_name = models.CharField(max_length = 225)
    street = models.CharField(max_length = 225)
    city = models.CharField(max_length = 225)
    state = models.CharField(max_length = 225)
    pincode = models.CharField(max_length = 225)
    salary = models.DecimalField(max_digits=10, decimal_places=2)



