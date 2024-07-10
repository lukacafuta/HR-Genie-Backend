from django.urls import path

from .views import UserProfileGetAll, UserProfileByApproverView, UserProfileDetailView

urlpatterns = [
    path('', UserProfileGetAll.as_view()),
    path('approvers/', UserProfileByApproverView.as_view()),
    path('<str:customUser__username>/', UserProfileDetailView.as_view()),
    #path('<int:pk>/', UserProfileGetAll.as_view()),
    # path('<int:pk>/', RecipeByIdView.as_view())
]