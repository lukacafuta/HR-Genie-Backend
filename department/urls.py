from django.urls import path

from department.views import UserDepartmentView, DepartmentUpdateView

urlpatterns = [
    path('user-department/', UserDepartmentView.as_view()),
    path('update-department/<int:pk>/', DepartmentUpdateView.as_view()),
]