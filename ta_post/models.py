from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="(Name + Schedule)")
    day1 = models.TextField(verbose_name="First Availability: (day/s: time)", blank=True)
    day2 = models.TextField(default='', verbose_name="Second Availability: (day/s: time)", blank=True)
    day3 = models.TextField(default='', verbose_name="Third Availability: (day/s: time)", blank=True)
    classes = models.TextField(blank=True, verbose_name="Classes: (list all)")
    about = models.TextField(blank=True, verbose_name="Description: (tell us about yourself)")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        default=1
        )

    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})