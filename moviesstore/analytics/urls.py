from django.urls import path
from . import views

urlpatterns = [
    path('top-purchaser/', views.top_purchaser, name='analytics.top_purchaser'),
    path('top-commenter/', views.top_commenter, name='analytics.top_commenter'),
]
