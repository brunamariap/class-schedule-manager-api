# Generated by Django 4.2.1 on 2023-05-30 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
        ('course', '0003_alter_schedule_weekday'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TeachTemporarily',
            new_name='TemporaryClass',
        ),
        migrations.AlterModelTable(
            name='temporaryclass',
            table='temporary_class',
        ),
    ]
