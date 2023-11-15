from django.db import models

# TODO: django-countries?
COUNTRY_CHOICES = [
    ("PL", "Poland"),
    ("CZ", "Czech Republic"),
    ("UK", "United Kingdom"),
    ("DE", "Germany"),
    ("US", "United States"),
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
    user_profile = models.OneToOneField(
        "user.UserProfile",
        on_delete=models.CASCADE,
        related_name="company",
        help_text="The user profile that this company is associated with.",
    )


class Counterparty(Company):
    user_profile = models.ForeignKey(
        "user.UserProfile",
        on_delete=models.CASCADE,
        related_name="counterparties",
        help_text="The user profile associated with this counterparty.",
    )
