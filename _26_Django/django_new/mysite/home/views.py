from django.http.response import HttpResponse
from django.shortcuts import render
from .models import User
def index(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = form.last_name
        email = form.email
        phone = form.phone
        location = form.location
    return render(request, 'index.html')

# Create your views here.
