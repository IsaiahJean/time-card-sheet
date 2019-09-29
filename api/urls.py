from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import ObtainAuthToken
<<<<<<< HEAD
from .views import UserViewSet
=======

>>>>>>> 5ddae3ea90fb26dfb6c9cd3b986eca70911470b3

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
<<<<<<< HEAD




=======
    path('auth/', ObtainAuthToken.as_view()),
>>>>>>> 5ddae3ea90fb26dfb6c9cd3b986eca70911470b3
]