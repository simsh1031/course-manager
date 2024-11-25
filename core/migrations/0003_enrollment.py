# Generated by Django 4.2 on 2024-11-18 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20241104_1304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enroll_date', models.DateField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.student')),
            ],
            options={
                'verbose_name': '수강 신청',
                'db_table': 'enrollment',
            },
        ),
    ]