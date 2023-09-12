# Generated by Django 4.2.2 on 2023-07-18 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название задачи')),
                ('description', models.TextField(verbose_name='Описание')),
                ('project_type', models.CharField(choices=[('L', 'Список'), ('S', 'Секции')], max_length=1, verbose_name='Тип проекта')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название секции')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section', to='todo.project', verbose_name='Проект')),
            ],
            options={
                'verbose_name': 'Секция',
                'verbose_name_plural': 'Секция',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название задачи')),
                ('description', models.TextField(verbose_name='Описание')),
                ('completed', models.BooleanField(default=False, verbose_name='Статус')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('time', models.TimeField(blank=True, verbose_name='Время выполнения')),
                ('date', models.DateTimeField(blank=True, verbose_name='Дата выполнения')),
                ('notification', models.DateTimeField(blank=True, verbose_name='Время уведомления')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_task', to='todo.project', verbose_name='Проект')),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='section_task', to='todo.section', verbose_name='Секция')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
    ]