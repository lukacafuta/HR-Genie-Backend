from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from companiesProfile.models import CompaniesProfile
from companiesProfile.serializers import CompaniesProfileSerializer
from userProfile.models import UserProfile


# Create your views here.
class UserCompanyProfile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user_profile = get_object_or_404(UserProfile, customUser=request.user)
        company = user_profile.company
        serializer = CompaniesProfileSerializer(company)
        return Response(serializer.data)


class IsCompanyAdmin:
    def has_permission(self, request, view):
        company_id = view.kwargs.get('pk')
        company = get_object_or_404(CompaniesProfile, pk=company_id)
        try:
            user_profile = UserProfile.objects.get(customUser=request.user, company=company)
            return user_profile.isCompanyAdmin
        except UserProfile.DoesNotExist:
            return False


class CompaniesProfileDetail(APIView):
    permission_classes = [IsAuthenticated, IsCompanyAdmin]

    def patch(self, request, pk, format=None):
        company = get_object_or_404(CompaniesProfile, pk=pk)
        serializer = CompaniesProfileSerializer(company, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
