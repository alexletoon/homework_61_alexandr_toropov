# Generated by Django 4.1 on 2022-10-11 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0003_rename_type_task_type_old'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, related_name='task', to='task_app.type', verbose_name='Тип задачи'),
        ),
        migrations.AlterField(
            model_name='task',
            name='type_old',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='task_set', to='task_app.type', verbose_name='Тип задачи'),
        ),
    ]
