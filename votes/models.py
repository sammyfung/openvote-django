from django.db import models

class Vote(models.Model):
  identity = models.CharField(max_length=128)
  vote_time = models.DateTimeField()
  question = models.PositiveSmallIntegerField()
  priority = models.PositiveSmallIntegerField()
  vote = models.PositiveSmallIntegerField()
