from django.urls import path

from .views import AbsenceGetAll, CreateListModifyAbsenceMeView

urlpatterns = [
    path('', AbsenceGetAll.as_view()),
    path('me/', CreateListModifyAbsenceMeView.as_view())
    # path('<int:pk>/', RecipeByIdView.as_view())
]