from django.db import models

class Batch(models.Model):
    batch_alpha_id = models.CharField(max_length=255)

class Object(models.Model):
    object_alpha_id = models.CharField(max_length=255, unique=True)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)

class Data(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255, null=True)
