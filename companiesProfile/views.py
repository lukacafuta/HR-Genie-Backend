from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from companiesProfile.models import CompaniesProfile
from companiesProfile.permissions import IsCompanyAdmin
from companiesProfile.serializers import CompaniesProfileSerializer
from userProfile.models import UserProfile


# Create your views here.
class UserCompanyProfileView(APIView):
    """
    Retrieve the info of the company of the logged-in user
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user_profile = get_object_or_404(UserProfile, customUser=request.user)
        company = user_profile.company
        serializer = CompaniesProfileSerializer(company)
        return Response(serializer.data)


class ListCreateCompaniesProfileView(ListCreateAPIView):
    """
    GET: List all company profiles (company admin)
    POST: Create a new company profile (company admin)
    """
    permission_classes = [IsAuthenticated, IsCompanyAdmin]
    serializer_class = CompaniesProfileSerializer
    queryset = CompaniesProfile.objects.all()


class RetrieveUpdateDeleteCompaniesProfileView(RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a single company profile by ID (company admin)
    PATCH: Update a single company profile by ID (company admin)
    DELETE: Delete a single company profile by ID (company admin)
    """
    permission_classes = [IsAuthenticated, IsCompanyAdmin]
    serializer_class = CompaniesProfileSerializer
    queryset = CompaniesProfile.objects.all()

