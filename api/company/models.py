from django.conf import settings
from django.db import models

# TODO: django-countries?
COUNTRY_CHOICES = [
    ("PL", "Poland"),
    ("US", "United States"),
    ("UK", "United Kingdom"),
    ("DE", "Germany"),
    ("FR", "France"),
]


class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    identification_number = models.CharField(
        max_length=50,
        unique=True,
        help_text="Company's official identification number (e.g., NIP, VAT, EIN)",
    )
    country = models.CharField(
        max_length=2,
        choices=COUNTRY_CHOICES,
        help_text="The country where the company is located",
    )

    class Meta:
        abstract = True


class UserCompany(Company):
    # TODO: Link it to UserProfile when there
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="company",
        help_text="The user that this company is associated with.",
    )


class Counterparty(Company):
    pass
