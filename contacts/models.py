from django.core.exceptions import ValidationError
from django.db import models

def validate_phone_number(value):
    if not value.isdigit() or len(value) != 10:
        raise ValidationError('Phone number must be exactly 10 digits.')

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    company = models.CharField(max_length=100)
    user = models.ForeignKey('accounts.User', related_name='contacts', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class PhoneNumber(models.Model):
    number = models.CharField(max_length=10, validators=[validate_phone_number])
    contact = models.ForeignKey(Contact, related_name='phone_numbers', on_delete=models.CASCADE)

    def __str__(self):
        return self.number
