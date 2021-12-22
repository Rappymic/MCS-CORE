
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.employee_form, name="index")
    path('list/', views.employee_list)
]
