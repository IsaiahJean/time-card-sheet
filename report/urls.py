from django.conf.urls import url
from .views import PostReport


urlpatterns = [
    url(r'', PostReport.as_view(), name="post_report"),
]
