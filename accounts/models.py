from django.db import models
from django.contrib.auth.models import AbstractUser


# Custom user model for TA accounts.
class CustomUser(AbstractUser):
    year = models.PositiveIntegerField(null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    hours = models.PositiveIntegerField(null=True, blank=True, verbose_name="total hours a week")
    DAY_OPTIONS = (
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'), 
		('WED', 'Wednesday'),
		('THU', 'Thursday'), 
		('FRI', 'Friday'),
    )
    is_ta = models.BooleanField(default=False)
    days_available = models.TextField(blank=True, verbose_name='Days Available')

    def set_days(self, days):
        self.days_available = ','.join(days)

    def get_days(self):
        if self.days_available:
            return self.days_available.split(',')
        else:
            return 
