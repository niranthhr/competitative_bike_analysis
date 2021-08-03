from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)



class appdetails_model(models.Model):

    names = models.CharField(max_length=300)
    App_desc= models.CharField(max_length=500)
    App_Uses = models.CharField(max_length=100)
    Memory_Required = models.CharField(max_length=300)
    Mobile_OS = models.CharField(max_length=300)
    Space_Needed = models.CharField(max_length=300)
    senderstatus = models.CharField(default="process", max_length=300 )
    ratings = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    sanalysis= models.CharField(max_length=300)
    DT = models.CharField(max_length=300)


class review_Model(models.Model):
    uname = models.CharField(max_length=100)
    ureview = models.CharField(max_length=100)
    sanalysis = models.CharField(max_length=100)
    dt= models.CharField(max_length=300)
    tname= models.CharField(max_length=300)
    suggestion = models.CharField(max_length=300)

class share_Model(models.Model):
    uname1 = models.CharField(max_length=100)
    appname = models.CharField(max_length=100)
    loc = models.CharField(max_length=100)
    dt= models.CharField(max_length=300)
    usefull= models.CharField(max_length=300)




