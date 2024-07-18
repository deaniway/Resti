from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'users.User'
        fields = ('username', 'password')
