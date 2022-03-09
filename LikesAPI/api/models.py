from django.db import models


class Picture(models.Model):
    id = models.BigIntegerField(primary_key=True)
    likes = models.BigIntegerField(default=0)
    dislikes = models.BigIntegerField(default=0)
    url = models.TextField(null=False)
