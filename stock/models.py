from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)

class Event(models.Model):
    init_date = models.DateTimeField('init date')
    end_date = models.DateTimeField('end date')
    name = models.CharField(max_length=200)
    user_name = models.ForeignKey(models.User)
    items = models.ManyToManyField(Item, through='ItemEvent')

class ItemEvent(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date_joined = models.DateField()
    number_of_items = models.IntegerField()