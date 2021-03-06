# Generated by Django 3.0.3 on 2021-02-13 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stud_no', models.CharField(default=None, help_text='Enter student number', max_length=10)),
                ('first_name', models.CharField(default=None, help_text='Enter first name', max_length=20)),
                ('last_name', models.CharField(help_text='Enter last name', max_length=20)),
                ('class_no', models.CharField(help_text='Enter class number', max_length=10)),
                ('age', models.IntegerField(help_text='enter student age', max_length=10)),
            ],
        ),
    ]
