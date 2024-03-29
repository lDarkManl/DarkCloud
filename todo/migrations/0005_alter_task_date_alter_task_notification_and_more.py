# Generated by Django 4.2.2 on 2023-07-18 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_task_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата выполнения'),
        ),
        migrations.AlterField(
            model_name='task',
            name='notification',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время уведомления'),
        ),
        migrations.AlterField(
            model_name='task',
            name='time',
            field=models.TimeField(blank=True, null=True, verbose_name='Время выполнения'),
        ),
    ]
