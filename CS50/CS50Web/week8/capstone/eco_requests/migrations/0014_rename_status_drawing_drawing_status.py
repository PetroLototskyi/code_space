# Generated by Django 5.1 on 2025-01-03 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("eco_requests", "0013_drawing_drawing_number_drawing_drawing_revision"),
    ]

    operations = [
        migrations.RenameField(
            model_name="drawing",
            old_name="status",
            new_name="drawing_status",
        ),
    ]
