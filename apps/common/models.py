from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class BaseModel(models.Model):
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    updated_at = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        abstract = True


class Contact(BaseModel):
    first_name = models.CharField('First name', max_length=150)
    last_name = models.CharField('Last_name', max_length=150)
    phone_number = PhoneNumberField("Phone number", max_length=32)
    text = models.TextField('Text')

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
