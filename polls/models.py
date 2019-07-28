from django.db import models


class Elevator(models.Model):
    comm_number = models.CharField(max_length=200)
    status_control = models.IntegerField(default=0)
    status_connection = models.IntegerField(default=0)


class ErrorHistory(models.Model):
    elevator = models.ForeignKey(Elevator, on_delete=models.CASCADE)
    LastError = models.CharField(max_length=200)
