from django.db import models

# Create your models here.
class Employee(models.Model):
    STANDARD = 'STD'
    MANAGER = 'MGR'
    CEO = 'CEO'
    EMPLOYEE_TYPES = ((STANDARD, 'base employee'),
                      (MANAGER, 'manager'),
                      (CEO, 'ceo'))
    emp_id = models.CharField(max_length=10, unique=True, primary_key=True)
    role = models.CharField(max_length=25, choices=EMPLOYEE_TYPES)
    emp_name = models.CharField(max_length=100)
    manager_name = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='employee')

    def __str__(self):
        return self.emp_name