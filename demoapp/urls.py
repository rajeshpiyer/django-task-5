from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.index),
    path('company-form/', views.company_form, name='company_form'),
    path('first-view/',views.first_view,name='first-view'),
    path('company/<int:company_id>/', views.CompanyDetailView.as_view(), name='company_detail'),
    path('employee-form/', views.employee_form, name='employee_form'),
    path('second-view/',views.second_view,name='second-view'),
    path('employee/<int:employee_id>/', views.EmployeeDetailView.as_view(), name='employee_detail'),
]