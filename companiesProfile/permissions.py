from django.shortcuts import get_object_or_404
from rest_framework import permissions
from companiesProfile.models import CompaniesProfile
from userProfile.models import UserProfile


class IsCompanyAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        company_id = view.kwargs.get('pk')

        if company_id:
            # retrieve the company profile using the company ID
            company = get_object_or_404(CompaniesProfile, pk=company_id)

            try:
                # check if the user is an admin of the given company
                user_profile = UserProfile.objects.get(customUser=request.user, company=company)
                return user_profile.isCompanyAdmin
            except UserProfile.DoesNotExist:
                return False
        else:
            return False
