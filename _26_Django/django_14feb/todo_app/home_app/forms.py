from django.forms import ModelForm
from .models import home_list

class Create_New(ModelForm):
    class Meta:
        model = home_list
        fields = '__all__'