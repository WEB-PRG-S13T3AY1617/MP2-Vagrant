from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Item(models.Model):
    item_poster = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    item_price = models.IntegerField()
    item_condition = models.IntegerField()
    item_quantity = models.IntegerField()
    OFFICE = 'OFFICE'
    ACADEMIC = 'ACADEMIC'
    TYPE_CHOICES = (
        (OFFICE, 'Office'),
        (ACADEMIC, 'Academic'),
    )
    item_type = models.CharField(max_length=15, choices = TYPE_CHOICES, default=OFFICE)
    item_academic_coursename = models.CharField(max_length=7)
    item_quantity = models.IntegerField()
    item_picture = models.FileField()

    def get_absolute_url(self):
        return reverse('items:detail', kwargs={'pk': self.pk})



# Create your models here.
