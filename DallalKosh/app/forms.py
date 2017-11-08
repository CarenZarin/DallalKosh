
from .models import *
from django import forms
from django.utils.translation import ugettext_lazy as _


class RequestedGoodForm(forms.ModelForm):
    class Meta:
        model = RequestedGood
        fields = [ "requestedgood_description" , "requestedgood_image" , "requestedgood_title" , "requestedgood_number"]


class RequestForm(forms.ModelForm):
    class Meta:
        model = Good
        fields = ["good_price", "good_description" , "good_title" , "good_image" , "good_number"]


