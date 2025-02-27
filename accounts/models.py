from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
import uuid

class CustomUser(AbstractUser):
    referral_code = models.CharField(max_length=20, unique=True, blank=True)
    referred_by = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)

    def save(self, *args, **kwargs):
        if not self.referral_code:
            self.referral_code = str(uuid.uuid4())[:8]
        super().save(*args, **kwargs)

class Referral(models.Model):
    referrer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="referrals")
    referred_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="referred")
    date_referred = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('successful', 'Successful')],
        default='pending'
    )

class Reward(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    points = models.PositiveIntegerField(default=0)

    def add_points(self, amount):
        self.points += amount
        self.save()
