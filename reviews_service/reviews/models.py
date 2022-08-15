from django.db import models


class Review(models.Model):
    body = models.TextField()
