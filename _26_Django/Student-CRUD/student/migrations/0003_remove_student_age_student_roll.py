# Generated by Django 4.0 on 2022-02-11 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_student_chemistry_student_maths_student_physics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
        migrations.AddField(
            model_name='student',
            name='roll',
            field=models.IntegerField(default='0'),
        ),
    ]