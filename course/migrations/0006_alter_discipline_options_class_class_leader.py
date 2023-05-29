# Generated by Django 4.2.1 on 2023-05-28 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_student_registration'),
        ('course', '0005_alter_discipline_options_alter_discipline_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discipline',
            options={},
        ),
        migrations.AddField(
            model_name='class',
            name='class_leader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='student.student'),
        ),
    ]
