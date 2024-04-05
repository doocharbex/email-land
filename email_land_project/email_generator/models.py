from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserLimit(models.Model):
    telegram_id = models.BigIntegerField(primary_key=True, default=None)
    email_count = models.IntegerField(default=2)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.telegram_id}: {self.email_count} emails left"



class EmailAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email_username = models.EmailField()
    email_password = models.CharField(max_length=400)
    email_quota = models.CharField(max_length=100)

    def __str__(self):
        return self.email_username