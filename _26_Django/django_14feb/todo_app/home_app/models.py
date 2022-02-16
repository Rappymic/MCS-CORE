from django.db import models

# Create your models here.
class home_list(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    date_created = models.DateField()
    time_completion = models.TimeField()

    def __str__(self):
        return self.title
