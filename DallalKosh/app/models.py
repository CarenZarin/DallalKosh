from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class RequestedGood(models.Model):
    """docstring fos RequestedGood"""
    requestedgood_user = models.ForeignKey(User)
    requestedgood_description = models.TextField(max_length=400, null=True)
    requestedgood_title = models.CharField(max_length=200, null=True)
    requestedgood_image = models.ImageField(blank=True, upload_to='reqgoodimages/', null=True)
    requestedgood_number = models.PositiveSmallIntegerField(blank=False, null=True)
    requestgood_data = models.DateTimeField(null=True  ,auto_now=True)


    def __str__(self):
        return "%s %s" % (self.requestedgood_title ,self.requestedgood_user)


class Good(models.Model):
    good_owner = models.ForeignKey(User)
    good_price = models.BigIntegerField()
    good_requestedgood = models.ForeignKey(RequestedGood)
    good_description = models.TextField(max_length=400, null=True)
    good_title = models.CharField(max_length=200, null=True)
    good_image = models.ImageField(blank=True, upload_to='goodimages/', null=True)
    good_number = models.PositiveSmallIntegerField(blank=False, null=True)
    good_data = models.DateTimeField(null=True  ,auto_now=True)

    def __str__(self):
        return "%s %s " % ( self.good_owner, self.good_title)



class OrderedGood(models.Model):
    orderedgood_good= models.ForeignKey(Good)
    orderedgood_date= models.DateTimeField(null=True)
    orderedgood_number= models.PositiveSmallIntegerField(null=True)
    orderedgood_total_price= models.BigIntegerField(null=True)