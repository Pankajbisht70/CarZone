from django.db import models
from datetime import datetime

from django.db.models.query_utils import PathInfo

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    car_id = models.IntegerField()
    customer_need = models.CharField(max_length=100)
    car_title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    #phone = models.IntegerField(blank=True, default=0)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=100)
    user_id = models.IntegerField()
    create_date = models.DateTimeField(blank=True, default=datetime.now)


    def __str__(self):
        return self.email
