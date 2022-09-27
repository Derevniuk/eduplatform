# Generated by Django 4.1 on 2022-09-24 20:23

import Eduplatform_site.mixins
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0007_create_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('is_open', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='learning.teacher')),
                ('topic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='learning.topic')),
            ],
            options={
                'verbose_name': 'topic_test',
                'verbose_name_plural': 'topic_tests',
            },
            bases=(models.Model, Eduplatform_site.mixins.DateTimeMixinModel),
        ),
    ]
