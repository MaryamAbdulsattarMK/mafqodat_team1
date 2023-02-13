from datetime import timedelta

from django.db import models
from django.utils import timezone

from helpers import models as modul

from mafqodatAPI import models as mod



class Type_item(models.Model):
    id = models.AutoField(primary_key=True)
    name_type = models.CharField(max_length=250)
    def __str__(self):
        return self.name_type








class location(models.Model):
    id = models.AutoField(primary_key=True)
    country=models.CharField(default="Iraq",max_length=255)
    City = models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    latitude=models.FloatField()
    longitude=models.FloatField()

    def __str__(self):
        return self.City
class Region(modul.TrackingModel):
    id = models.AutoField(primary_key=True)
    city= models.ForeignKey( location,on_delete=models.CASCADE,default=5)
    Region= models.CharField(max_length=255)
    def __str__(self):
        return self.Region

def in_three_days():
    return timezone.now() + timedelta(days=3)


class PostTimeDetail(models.Model):
    id = models.AutoField(primary_key=True)
   # Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    expierd_at = models.DateTimeField(default=in_three_days)
    edits_time = models.IntegerField(default=1)



class Post(modul.TrackingModel):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='photo/%y/%m/%d',default='default/1.png')
    location = models.ForeignKey(Region, on_delete=models.CASCADE,default=1)
    phone_number = models.IntegerField(default=12345)
    #By_user= models.ForeignKey(mod.myUser,on_delete=models.CASCADE,default=mod.myUser.id)
    Date = models.DateField(auto_created=True,default=timezone.now)
    chat_count = models.IntegerField(default=1)
    Action = models.TextField(default="default")
    type = models.ForeignKey(Type_item, on_delete=models.CASCADE,default=1)
    is_checked_by_admin = models.BooleanField(default=False)
    PostDetail = models.OneToOneField(PostTimeDetail,on_delete=models.CASCADE)
    #PostDetail = models.ForeignKey(PostTimeDetail, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.Name






