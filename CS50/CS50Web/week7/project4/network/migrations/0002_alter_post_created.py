# Generated by Django 5.1 on 2024-12-05 17:32

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="created",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
