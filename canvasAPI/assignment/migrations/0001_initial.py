# Generated by Django 3.0.6 on 2020-05-19 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=500)),
                ('grade', models.FloatField()),
                ('deadline', models.DateField()),
            ],
        ),
    ]
