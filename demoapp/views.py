from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import Company,Employee
from demoapp.forms import CompanyForm,EmployeeForm

def index(request):
    return render(request,'index.html')

#COMPANY INPUT VIEW
def company_form(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company_instance = Company(
                name=form.cleaned_data['name'],
                location=form.cleaned_data['location'],
                employee_count=form.cleaned_data['employee_count'],
                office_count=form.cleaned_data['office_count'],
                turnover=form.cleaned_data['turnover']
            )
            
            company_instance.save()
            return index(request)
    else:
        form = CompanyForm()
    return render(request, 'company_form.html', {'form_company': form})

#EMPLOYEE INPUT VIEW
def employee_form(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return index(request)
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})



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


