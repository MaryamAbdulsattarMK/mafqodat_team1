from django.db import models
from django.utils import timezone

from helpers import models as modul

# Create your models here.

class Post(modul.TrackingModel):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='photos/%y/%m/%d',default='default/1.png')
    location = models.CharField(max_length=250)
    phone_number = models.IntegerField()
    By_user= models.TextField()
    Date = models.DateField(auto_created=True,default=timezone.now)
    chat_count = models.IntegerField()
    Action = models.TextField()

    def __str__(self):
        return self.Name

