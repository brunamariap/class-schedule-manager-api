# Generated by Django 4.2.1 on 2023-05-30 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
        ('course', '0007_alter_classcanceled_teachers_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classcanceled',
            name='teachers_id',
        ),
        migrations.AddField(
            model_name='classcanceled',
            name='teacher_ids',
            field=models.ManyToManyField(blank=True, db_column='teacher_ids', db_table='substitute_teachers', null=True, to='teacher.teacher'),
        ),
    ]
