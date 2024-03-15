from django import forms
from .models import Employee

class CompanyForm(forms.Form):
    name = forms.CharField(max_length=225)
    location = forms.CharField(max_length=125)
    employee_count = forms.IntegerField(initial=0)
    office_count = forms.IntegerField(initial=0)
    turnover = forms.IntegerField(initial=0)

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'