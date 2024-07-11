from django.urls import path

#from .views import UserProfileGetAll, UserProfileByApproverView
from .views import UserProfileGetAll, ListUserProfileMeView, UserProfileByApproverView

urlpatterns = [
    path('', UserProfileGetAll.as_view()),
    path('approvers/', UserProfileByApproverView.as_view()),
    #path('<int:pk>/', UserProfileGetAll.as_view()),
    # path('<int:pk>/', RecipeByIdView.as_view())
    path('me/', ListUserProfileMeView.as_view()),
]