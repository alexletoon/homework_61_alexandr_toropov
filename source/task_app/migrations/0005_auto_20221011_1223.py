# Generated by Django 4.1 on 2022-10-11 12:23

from django.db import migrations



def transfer_tags(apps, schema_editor):

    Task = apps.get_model('task_app.Task')

    for task in Task.objects.all():

        task.tags.set(task.type_old.all())





def rollback_transfer(apps, schema_editor):

    Task = apps.get_model('task_app.Task')

    for task in Task.objects.all():

        task.tags_old.set(task.type.all())




class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0004_task_type_alter_task_type_old'),
    ]

    operations = [
    ]
