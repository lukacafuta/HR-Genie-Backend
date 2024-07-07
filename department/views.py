from django.shortcuts import render, get_object_or_404
from rest_framework import status
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


class DepartmentUpdateView(APIView):
    """
    Edit department info (only by company admin)
    """
    permission_classes = [IsAuthenticated, IsCompanyAdmin]

    def patch(self, request, pk, format=None):
        department = get_object_or_404(Department, pk=pk)
        serializer = DepartmentSerializer(department, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
