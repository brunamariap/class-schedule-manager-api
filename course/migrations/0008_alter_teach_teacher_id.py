# Generated by Django 4.2.1 on 2023-05-29 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_alter_teacher_registration'),
        ('course', '0007_alter_class_course_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teach',
            name='teacher_id',
            field=models.ForeignKey(db_column='teacher_id', on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher'),
        ),
    ]
