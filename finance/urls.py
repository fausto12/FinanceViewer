from django.urls import path
from . import views

app_name = "finance"


urlpatterns = [
    path('', views.FinancesPage.as_view(), name='finances')
]
