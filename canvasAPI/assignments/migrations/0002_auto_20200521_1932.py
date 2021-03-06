# Generated by Django 3.0.6 on 2020-05-22 01:32

import assignments.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('assignments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='grade',
        ),
        migrations.AddField(
            model_name='assignment',
            name='assignment_file',
            field=models.FileField(blank=True, upload_to=assignments.models.user_directory_path),
        ),
        migrations.AddField(
            model_name='assignment',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.Course'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='score',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
