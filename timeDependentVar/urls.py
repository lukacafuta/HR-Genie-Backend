from django.urls import path

from timeDependentVar.views import UserProfileDetailView

urlpatterns = [
    path('<str:customUser__username>/', UserProfileDetailView.as_view()),
]