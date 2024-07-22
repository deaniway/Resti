from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email')
        extra_kwargs = { 'password': {'write_only': True} }

    def create(self, validated_data):
        user = get_user_model()(
            username=validated_data["username"],
            email=validated_data["email"]
        )
        user.set_password( validated_data["password"] )
        user.save()
        return user
