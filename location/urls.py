
from django.contrib import admin
from django.urls import path
from .views import LocationList, LocationDetail

urlpatterns = [

    path(r'', LocationList.as_view(), name="location_list"),
    path(r'<int:pk>/', LocationDetail.as_view(), name="location_detail"),
]