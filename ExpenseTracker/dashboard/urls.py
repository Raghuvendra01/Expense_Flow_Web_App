from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('save-budget/', views.save_budget, name='save_budget'),
    path('logout/', views.logout_view, name='logout')
]