from django.db import models
from django.utils import timezone


class MainTable(models.Model):
    build = models.CharField('build', max_length=10)
    task = models.CharField('task', max_length=25)
    database = models.CharField('database', max_length=15)
    hash = models.CharField('hash', max_length=255)
    author = models.CharField('author', max_length=255)
    date = models.DateTimeField()
    message = models.TextField('message')
    filename = models.TextField('filename')
    add_date = models.DateTimeField(null=True, default=timezone.now)

    class Meta:
        db_table = "maintable"

