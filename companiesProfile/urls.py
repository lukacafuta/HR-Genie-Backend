from django.urls import path

from companiesProfile.views import CompaniesProfileDetail, UserCompanyProfile

urlpatterns = [
    path('my-company/', UserCompanyProfile.as_view()),
    path('<int:pk>/',  CompaniesProfileDetail.as_view()),
]