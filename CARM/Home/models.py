from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.
class Users_log(models.Model):
    userid=models.CharField(max_length=10)
    password=models.CharField(max_length=15)
    role = models.CharField(
        max_length=20,
        choices=[("admin", "Admin"), ("staff", "Staff"), ("user", "User")],
        default="user"
    )
    failed_attempts = models.IntegerField(default=0)
    lock_until = models.DateTimeField(null=True, blank=True)

    def is_locked(self):
        if self.lock_until and timezone.now() < self.lock_until:
            return True
        return False
    
    def reset_attempt(self):
        self.failed_attempts=0
        self.lock_until=None
        self.save()
