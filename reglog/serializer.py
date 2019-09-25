from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username']
        extra_kwargs = {'password': {"write_only": True, "required": True}}

    def create(self, validated_data):
        user = User.Objects.create_user(**validated_data)
        return user