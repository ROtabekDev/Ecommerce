from django.db import models


class CurrencyType(models.TextChoices):
    UZS = "uzs", "Uzbekistan som"
    RUB = "rub", "Russian ruble"
    USD = "usd", "US dollor"
    EUR = "eur", "Euro"
