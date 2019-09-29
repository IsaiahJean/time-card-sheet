from django.contrib.auth.models import User
from rest_framework import serializers
<<<<<<< HEAD
from rest_framework.authtoken.models import Token
=======
>>>>>>> 5ddae3ea90fb26dfb6c9cd3b986eca70911470b3


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
<<<<<<< HEAD
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
=======
        fields = ['username', 'password', 'first_name', 'last_name']
        extra_kwargs ={'password': {'write_only': True, 'required': True}}


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user






>>>>>>> 5ddae3ea90fb26dfb6c9cd3b986eca70911470b3
