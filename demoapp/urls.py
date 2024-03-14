from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.index),
    path('first-view/',views.first_view),
    path('company/<int:company_id>/', views.CompanyDetailView.as_view(), name='company_detail'),
    path('second-view/',views.second_view),
    path('employee/<int:employee_id>/', views.EmployeeDetailView.as_view(), name='employee_detail'),
]