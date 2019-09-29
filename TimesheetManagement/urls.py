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
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    url(r'^admin/', admin.site.urls),
<<<<<<< HEAD
    url(r'^timecards/', include(('timeCard.urls', 'timeCard'), namespace='timeCard')),
    url(r'^doctors/', include(('doctor.urls', 'doctor'), namespace='doctor')),
    url(r'^locations/', include(('location.urls', 'location'), namespace='location')),
    url(r'^api/', include('api.urls')),
    url(r'^auth/', ObtainAuthToken.as_view())


=======
    url(r'^timecards/', include(('timeCard.urls', 'timeCard'), namespace='timeCard')),  # TimeCard app, see TimeCard.urls for more options
    url(r'^users/', include(('admin_users.urls', 'admin_users'), namespace='admin_users')),  # admin_users app, see admin_users.urls for more options
	url(r'^doctors/', include(('doctor.urls', 'doctor'), namespace='doctor')),  # doctors app
    url(r'^locations/', include(('location.urls', 'location'), namespace='location')),  # location app
    url(r'^report/', include(('report.urls', 'report'), namespace='report')),  # get report
    url(r'^api/', include('api.urls')),
>>>>>>> 5ddae3ea90fb26dfb6c9cd3b986eca70911470b3
]
