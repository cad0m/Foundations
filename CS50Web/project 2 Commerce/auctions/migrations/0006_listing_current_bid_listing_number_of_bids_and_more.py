# Generated by Django 5.0.7 on 2024-09-03 06:43

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0005_alter_watchlist_unique_together"),
    ]

    operations = [
        migrations.AddField(
            model_name="listing",
            name="current_bid",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                max_digits=6,
                validators=[django.core.validators.MinValueValidator(0.01)],
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="listing",
            name="number_of_bids",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="listing",
            name="winner",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="winnners",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="listing",
            name="starting_bid",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=6,
                validators=[django.core.validators.MinValueValidator(0.01)],
            ),
        ),
    ]
