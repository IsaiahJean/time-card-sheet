"""TimesheetManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^timecards/', include(('timeCard.urls', 'timeCard'), namespace='timeCard')),  # TimeCard app, see TimeCard.urls for more options
    url(r'^users/', include(('admin_users.urls', 'admin_users'), namespace='admin_users')),  # admin_users app, see admin_users.urls for more options
    url(r'^api/', include(('angularapi.urls', 'angularapi'), namespace='angularapi')),  # Locations' and doctors' stuff
    url(r'^$', include(('reglog.urls', 'reglog'), namespace='reglog')),  # Login
]
