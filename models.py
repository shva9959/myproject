from django.db import models
from django.utils import timezone


class Vehicle(models.Model):
    v_id = models.PositiveIntegerField(null=True)
    dtstamp = models.DateTimeField(default=timezone.now)
    v_regnNo = models.CharField(max_length=20, blank=False, null=False)
    v_model = models.CharField(max_length=20, blank=False, null=False)
    v_make = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.v_id
