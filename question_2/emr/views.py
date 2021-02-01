from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

# Create your views here.
class EmployeeList(APIView):
    def get(self, request):

        model = Employee.objects.all()
        serializer = UsersSerializer(model, many=True)
        return Response(serializer.data)
