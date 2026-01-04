from django.urls import path
from .views import general

urlpatterns = [
    path('tests/', general.Tests, name='tests'),
]