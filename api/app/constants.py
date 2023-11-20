COUNTRY_CURRENCY_MAP = {
    "PL": ("Poland", "PLN"),
    "CZ": ("Czech Republic", "CZK"),
    "UK": ("United Kingdom", "GBP"),
    "DE": ("Germany", "EUR"),
    "US": ("United States", "USD"),
    "FR": ("France", "EUR"),
}

COUNTRY_CHOICES = [
    (code, name) for code, (name, currency) in COUNTRY_CURRENCY_MAP.items()
]

unique_currencies = set(currency for (name, currency) in COUNTRY_CURRENCY_MAP.values())
CURRENCY_CHOICES = [(currency, currency) for currency in unique_currencies]
