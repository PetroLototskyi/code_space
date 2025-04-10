# Generated by Django 5.1 on 2024-09-26 15:11

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0007_alter_auction_listing_created"),
    ]

    operations = [
        migrations.AddField(
            model_name="auction_listing",
            name="watchlist",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="item_watchlist",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="auction_listing",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 9, 26, 15, 11, 38, 966832)
            ),
        ),
    ]
