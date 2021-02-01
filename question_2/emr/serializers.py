from rest_framework import serializers
from emr.models import Employee

class UsersSerializer(serializers.ModelSerializer):
    emp_id = serializers.CharField(required=False)
    emp_name = serializers.CharField(required=False)
    manager_name = serializers.CharField(required=False)
    class Meta:
        model = Employee
        fields = ('emp_id', 'emp_name', 'manager_name')