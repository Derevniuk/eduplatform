# Generated by Django 4.0.6 on 2022-08-16 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_group_photo_alter_student_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='completed_tests',
            field=models.JSONField(default=dict),
        ),
    ]
