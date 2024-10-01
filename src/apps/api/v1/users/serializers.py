from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email')
        extra_kwargs = { 'password': {'write_only': True} }

    def create(self, validated_data):

        username = validated_data.get("username", None)
        password = validated_data.get("password", None)
        email = validated_data.get("email", None)

        if username is None or password is None or email is None:
            return None

        user = self.Meta.model(
            username=username,
            email=email
        )
        user.set_password( password )
        user.save()
        return user
