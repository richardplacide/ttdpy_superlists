from django.db import models

class List(models.Model):
    name = models.TextField(max_length=100)

class Item(models.Model):
    text = models.TextField(max_length=100)
    list = models.ForeignKey(List)
