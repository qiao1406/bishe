from django.db import models


class Record(models.Model):
    time = models.DateTimeField()
    sensor = models.CharField(max_length=255)
    val = models.FloatField()

    class Meta:
        unique_together = (('time', 'sensor'),)
