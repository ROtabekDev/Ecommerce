from django.db import models


class BuyigType(models.TextChoices):
    Self = "Self", "Self"
    Delivery = "Delivery", "Delivery"


class OrderStatus(models.TextChoices):
    New = "New",  "New"
    In_progress = "In_progress", "In progress"
    Error = "Error", "Error"
    Completed = "Completed", "Completed"
