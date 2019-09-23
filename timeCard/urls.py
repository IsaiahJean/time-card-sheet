from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<card_id>\d+)/$', views.gudTimeCard),
    url(r'^', views.gaTimeCards),
]