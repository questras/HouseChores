# Generated by Django 2.2.5 on 2019-09-09 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_task_done_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_done_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='done date'),
        ),
    ]
