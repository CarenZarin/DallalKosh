from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile

class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')
    myprofile_company_address= models.CharField(max_length=400 , null=True)
    myprofile_company_name= models.CharField(max_length=50 , null=True)
    myprofile_company_phonenumber= models.CharField(max_length=11 ,null=True)
    myprofile_fullname= models.CharField(max_length=70 , null=True)
    myprofile_is_seller= models.BooleanField(default=False)
