"""DallalKosh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from .app import views

from django.conf.urls.static import static
from . import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^customer/request/$',views.requestedgood ),
    url(r'^provider/customersrequests/$', views.customers_requests),

    url(r'^entertobazar$',views.entertobazar),

    url(r'^provider/offer/$', views.provider_offer),
    url(r'^provider/goods/$', views.provider_goods),
    url(r'^customer/requestlist/$', views.customer_requestlist),
    url(r'^customer/final_choose/$', views.customer_final_choose),
    url(r'^factor/$', views.factor),
    url(r'^mycompanygoods/$', views.show_company_goods),

    url(r'^accounts/', include('DallalKosh.accounts.urls')),
    url(r'^$', views.root),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
