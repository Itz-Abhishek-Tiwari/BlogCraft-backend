from rest_framework import serializers
from django.contrib.auth.models import User
# from rest_framework.response import Response
# from rest_framework.validators import UniqueValidator
# from django.contrib.auth.password_validation import validate_password


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class ResgisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)  # Fixed typo here

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "password2",
            "email",
            "first_name",
            "last_name",
        ]

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError("password does not match")
        return attrs

    def create(self, validated_data):
        validated_data.pop("password2")
        user = User.objects.create_user(**validated_data)
        return user
