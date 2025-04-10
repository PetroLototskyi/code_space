# Generated by Django 5.1 on 2024-09-21 15:11

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0005_category_alter_auction_listing_created"),
    ]

    operations = [
        migrations.AddField(
            model_name="auction_listing",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="auction_listing",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="category",
                to="auctions.category",
            ),
        ),
        migrations.AlterField(
            model_name="auction_listing",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 9, 21, 15, 11, 35, 464083)
            ),
        ),
    ]
