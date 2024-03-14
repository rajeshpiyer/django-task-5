from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import Company,Employee

def index(request):
    return render(request,'index.html')

#COMPANY LIST VIEW
def first_view(request):
    companies = Company.objects.all()
    return render(request, 'first-view.html', {'companies': companies})

#COMPANY DETAIL VIEW
class CompanyDetailView(View):
    def get(self,request,company_id,*args,**kwargs):
        company = get_object_or_404(Company, id=company_id)
        return render(request, 'company_detail.html', {'company': company})
    
#EMPLOYEE LIST VIEW
def second_view(request):
    employees = Employee.objects.all()
    return render(request, 'second-view.html', {'employees': employees})

#EMPLOYEE DETAIL VIEW
class EmployeeDetailView(View):
    def get(self,request,employee_id,*args,**kwargs):
        employee = get_object_or_404(Employee, id=employee_id)
        return render(request, 'employee_detail.html', {'employee': employee})


