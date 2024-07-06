from django.urls import path

from .views import UserProfileGetAll, ListUserProfileMeView

urlpatterns = [
    path('', UserProfileGetAll.as_view()),
    path('me/', ListUserProfileMeView.as_view()),
]