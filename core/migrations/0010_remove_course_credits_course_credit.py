# Generated by Django 4.2 on 2024-11-18 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_course_credits_enrollment_semester_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='credits',
        ),
        migrations.AddField(
            model_name='course',
            name='credit',
            field=models.IntegerField(default=3),
        ),
    ]