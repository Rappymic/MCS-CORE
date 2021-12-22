from django.shortcuts import render

# Create your views here.
def employee_list(request):
    return render(request, 'emp_register/emp_list.html')

def employee_form(request):
    return render(request, 'emp_register/emp_form.html')


def employee_delete(request):
    pass