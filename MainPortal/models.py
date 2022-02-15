from django.db import models


class Settings(models.Model):
    p = models.IntegerField(default=1, primary_key=True)
    email = models.EmailField()
    paypal_email = models.EmailField(null=True, blank=True)
    paypal_password = models.CharField(max_length=250, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    checking_interval = models.IntegerField()


class Website(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    account_email = models.EmailField()
    account_password = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    url = models.URLField()
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    size = models.CharField(max_length=20, null=True, blank=True)
    color = models.CharField(max_length=20, null=True, blank=True)
    is_available = models.BooleanField(default=False, null=True, blank=True)
    is_purchased = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name
