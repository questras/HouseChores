# Generated by Django 2.2.5 on 2019-09-09 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date added')),
                ('due_date', models.DateTimeField(verbose_name='due date')),
                ('task_giver', models.CharField(max_length=50)),
                ('task_done_by', models.CharField(max_length=50)),
            ],
        ),
    ]
