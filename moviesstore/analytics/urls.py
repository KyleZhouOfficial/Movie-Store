from django.urls import path
from . import views

urlpatterns = [path('top-purchaser/', views.top_purchaser, name='analytics.top_purchaser')]