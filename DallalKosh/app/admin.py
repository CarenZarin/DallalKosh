from django.contrib import admin
from .models import *
# Register your models here.


class Good_admin(admin.ModelAdmin):
    # fields=['btime','utime']
    readonly_fields=['good_date']
    class Meta:
        model=Good
admin.site.register(Good,Good_admin)

admin.site.register(RequestedGood)
# admin.site.register(Good)

