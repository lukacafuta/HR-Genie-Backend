from django.urls import path

from .views import UserProfileGetAll

urlpatterns = [
    path('', UserProfileGetAll.as_view()),
    #path('<int:pk>/', UserProfileGetAll.as_view()),
    # path('<int:pk>/', RecipeByIdView.as_view())
]