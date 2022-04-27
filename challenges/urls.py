from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('<int:month>', views.monthy_challenges_num),
    path('<str:month>', views.monthly_challenges, name='month-challenge'),
]