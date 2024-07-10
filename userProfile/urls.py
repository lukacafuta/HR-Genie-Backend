from django.urls import path

from .views import UserProfileGetAll, UserProfileByApproverView

urlpatterns = [
    path('', UserProfileGetAll.as_view()),
    path('approvers/', UserProfileByApproverView.as_view()),
    #path('<int:pk>/', UserProfileGetAll.as_view()),
    # path('<int:pk>/', RecipeByIdView.as_view())
]