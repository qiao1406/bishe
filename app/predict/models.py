from django.db import models


class Record(models.Model):
    time = models.DateTimeField()
    sensor = models.CharField(max_length=255)
    val = models.FloatField()

    class Meta:
        unique_together = (('time', 'sensor'),)


class ModelRecord(models.Model):
    model_name = models.CharField(max_length=255)
    observe_window = models.IntegerField()
    predict_gap = models.IntegerField()
    predict_len = models.IntegerField()
    para_d = models.IntegerField()
    para_r = models.IntegerField()
    file_path = models.CharField(max_length=255)

    class Meta:
        unique_together = (('model_name', 'observe_window', 'predict_gap', 'predict_len', 'para_d', 'para_r'),)
