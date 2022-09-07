# Generated by Django 4.0.6 on 2022-08-23 17:57

import django.db.models.deletion
from django.db import migrations, models

import Eduplatform_site.mixins


class Migration(migrations.Migration):

    dependencies = [
        ("learning", "0005_create_question_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="Answer",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("text", models.CharField(blank=True, max_length=50, null=True)),
                ("is_correct", models.BooleanField(default=False)),
                ("question", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="learning.question")),
            ],
            options={
                "verbose_name": "question_answer",
                "verbose_name_plural": "question_answers",
            },
            bases=(models.Model, Eduplatform_site.mixins.DateTimeMixinModel),
        ),
    ]
