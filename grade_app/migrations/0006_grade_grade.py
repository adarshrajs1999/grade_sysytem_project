# Generated by Django 5.0.7 on 2024-08-02 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade_app', '0005_remove_course_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='grade',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
