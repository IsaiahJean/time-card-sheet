
from django.contrib import admin
from django.conf.urls import url, include
from .views import LocationList

urlpatterns = [

    url(r'', LocationList.as_view(), name="location_list"),

]