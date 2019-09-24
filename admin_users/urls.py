from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^users/$', views.g_users),  # Get all users with description
    url(r'^p_user/$', views.p_user),  # Add user without description
    url(r'^g_user/(?P<username>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', views.g_user),  # Get user without description by username
    url(r'^add_description/$', views.p_description),  # Add description to user
]
