# Generated by Django 5.2.1 on 2025-06-02 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_student_college_faculty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='salary',
        ),
    ]
