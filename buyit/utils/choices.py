from django.db import models

class Gender(models.TextChoices):
    Male = ("male", "Male")
    Female = ("female", "Female")
    Other = ("other", "Other")


class CartStatus(models.TextChoices):
    Pending = ("Pending", "Pending")
    Completed = ("Completed", "Completed")


class AddressChoices(models.TextChoices):
    Billing = ("Billing", "Billing")
    Shipping = ("Shipping", "Shipping")


class PaymentChoices(models.TextChoices):
    PayPal = ("PayPal", "PayPal")
    Flutterwave = ("Flutterwave", "Flutterwave")
    Paystack = ("Paystack", "Paystack")
    Kuda = ("Kuda", "Kuda")
