from django.urls import path


from .views import ComputeKpiYearlyMe


urlpatterns = [
    #path('me/', calculate_kpi, name='calculate_kpi'),
    path('yearly/me/', ComputeKpiYearlyMe.as_view()),
]