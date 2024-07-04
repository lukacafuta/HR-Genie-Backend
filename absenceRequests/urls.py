from django.urls import path

from .views import AbsenceGetAll

urlpatterns = [
    path('', AbsenceGetAll.as_view()),
    # path('<int:pk>/', RecipeByIdView.as_view())
]