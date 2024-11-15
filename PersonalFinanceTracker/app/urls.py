# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add_income/', views.add_income, name='add_income'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('delete_income/<int:pk>/', views.delete_income, name='delete_income'),
    path('delete_expense/<int:pk>/', views.delete_expense, name='delete_expense'),
]
