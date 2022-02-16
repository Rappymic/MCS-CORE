from django.db import models
from django.urls import reverse
from django.db.models import Avg
class Student(models.Model):
    name = models.CharField(max_length=200)
    roll = models.IntegerField(default='0')
    section = models.CharField(max_length=200)
    physics = models.IntegerField(default='0')
    chemistry = models.IntegerField(default='0')
    maths = models.IntegerField(default='0')
    average = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default=None)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('student:student_edit', kwargs={'pk': self.pk})
