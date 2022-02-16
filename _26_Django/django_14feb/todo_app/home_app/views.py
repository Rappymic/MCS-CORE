from django.shortcuts import render, HttpResponse
from .models import home_list
# Create your views here.
from .forms import Create_New

def home_page(request):
    post_object = home_list.objects.all()
    form = Create_New()
    context = {
        'home_list_value' : post_object,
        'form' : form
    }
    if request.method == 'POST':
        print('Printing Post ', request.POST)
    return render(request, 'home_list/index.html', context)

