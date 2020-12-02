from django.urls import path 
from .views import guess_luck

urlpatterns = [
    path('', guess_luck)
]