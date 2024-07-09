from django.shortcuts import render, get_object_or_404
from rest_framework import status, generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from department.models import Department
from department.permissions import IsCompanyAdmin
from department.serializers import DepartmentSerializer
from userProfile.models import UserProfile


# Create your views here.
class UserDepartmentView(APIView):
    """
    Retrieve information about the department of the logged-in user
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user_profile = get_object_or_404(UserProfile, customUser=request.user)
        department = user_profile.department
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)


class ListCreateDepartmentsView(ListCreateAPIView):

    """
    GET: List all departments (company admin)
    POST: Create a new department (company admin)
    """

    permission_classes = [IsAuthenticated, IsCompanyAdmin]
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class RetrieveUpdateDeleteDepartmentsView(RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a single department by ID (company admin)
    PATCH: Update a single department by ID (company admin)
    DELETE: Delete single department by ID (company admin)
    """

    permission_classes = [IsAuthenticated, IsCompanyAdmin]
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
