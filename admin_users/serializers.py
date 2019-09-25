from rest_framework import serializers
from . models import UserDescription
from django.contrib.auth.models import User

# Serialize User object from auth_user
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

# Serialize description, used to get all users with description
class UserDescrSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserDescription
        fields = '__all__'

# Serializer that was used to add description
class AddDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDescription
        fields = "__all__"

# Serializer that was used to serialize description in edit description view
class ESerializer(serializers.ModelSerializer):

    class Meta:
        model = UserDescription
        fields = ('id', 'description')
