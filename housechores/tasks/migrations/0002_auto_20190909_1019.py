# Generated by Django 2.2.5 on 2019-09-09 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_done_by',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
