# Generated by Django 4.2.7 on 2023-11-09 16:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0002_refreshtoken"),
    ]

    operations = [
        migrations.CreateModel(
            name="AccessToken",
            fields=[
                (
                    "sid",
                    models.UUIDField(editable=False, primary_key=True, serialize=False),
                ),
                ("token", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="RefreshToken",
        ),
    ]