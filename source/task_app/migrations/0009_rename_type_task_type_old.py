# Generated by Django 4.1.2 on 2022-10-13 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0008_task_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='type',
            new_name='type_old',
        ),
    ]
