from django.db import models
from django.utils import timezone

from helpers import models as modul

# Create your models here.


class Type_item(models.Model):
    id = models.AutoField(primary_key=True)
    name_type = models.CharField(max_length=250)
    def __str__(self):
        return self.name_type

class Post(modul.TrackingModel):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='photo/%y/%m/%d',default='default/1.png')
    location = models.CharField(max_length=250)
    phone_number = models.IntegerField(default=12345)
    By_user= models.BooleanField(default=False)
    Date = models.DateField(auto_created=True,default=timezone.now)
    chat_count = models.IntegerField(default=1)
    Action = models.TextField(default="default")
    type_id = models.ForeignKey(Type_item, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.Name

