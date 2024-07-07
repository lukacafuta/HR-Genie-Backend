from django.urls import path

from companiesProfile.views import UserCompanyProfileView, CompaniesProfileUpdateView

urlpatterns = [
    path('user-company/', UserCompanyProfileView.as_view()),
    path('update-company/<int:pk>/',  CompaniesProfileUpdateView.as_view()),
]