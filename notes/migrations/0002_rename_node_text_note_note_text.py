# Generated by Django 4.2.2 on 2023-06-30 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='node_text',
            new_name='note_text',
        ),
    ]
