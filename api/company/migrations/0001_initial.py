# Generated by Django 4.2.7 on 2023-11-20 16:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("user", "0005_userprofile"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserCompany",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("address", models.TextField()),
                (
                    "identification_number",
                    models.CharField(
                        help_text="Company's official identification number (e.g., NIP, VAT, EIN)",
                        max_length=50,
                        unique=True,
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        choices=[
                            ("PL", "Poland"),
                            ("CZ", "Czech Republic"),
                            ("UK", "United Kingdom"),
                            ("DE", "Germany"),
                            ("US", "United States"),
                            ("FR", "France"),
                        ],
                        help_text="The country where the company is located",
                        max_length=2,
                    ),
                ),
                (
                    "user_profile",
                    models.OneToOneField(
                        help_text="The user profile that this company is associated with.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="company",
                        to="user.userprofile",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Counterparty",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("address", models.TextField()),
                (
                    "identification_number",
                    models.CharField(
                        help_text="Company's official identification number (e.g., NIP, VAT, EIN)",
                        max_length=50,
                        unique=True,
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        choices=[
                            ("PL", "Poland"),
                            ("CZ", "Czech Republic"),
                            ("UK", "United Kingdom"),
                            ("DE", "Germany"),
                            ("US", "United States"),
                            ("FR", "France"),
                        ],
                        help_text="The country where the company is located",
                        max_length=2,
                    ),
                ),
                (
                    "user_profile",
                    models.ForeignKey(
                        help_text="The user profile associated with this counterparty.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="counterparties",
                        to="user.userprofile",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
