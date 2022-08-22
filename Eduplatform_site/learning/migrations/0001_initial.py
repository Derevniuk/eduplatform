# Generated by Django 4.0.6 on 2022-08-15 20:34

import account.mixins
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'course',
                'verbose_name_plural': 'courses',
            },
            bases=(models.Model, account.mixins.DateTimeMixinModel),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=50)),
                ('numbering', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Min number value!')])),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning.course')),
            ],
            options={
                'verbose_name': 'course_topic',
                'verbose_name_plural': 'course_topics',
                'ordering': ['numbering'],
            },
            bases=(models.Model, account.mixins.DateTimeMixinModel),
        ),
    ]
