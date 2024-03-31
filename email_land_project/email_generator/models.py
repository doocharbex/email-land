from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserLimit(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_count = models.IntegerField(default=2)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username


class EmailAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email_username = models.EmailField()
    email_password = models.CharField(max_length=400)
    email_quota = models.CharField(max_length=100)

    def __str__(self):
        return self.email_username