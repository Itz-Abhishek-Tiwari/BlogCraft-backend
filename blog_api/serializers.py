from rest_framework import serializers
from .models import Post, Category
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
    categorys = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ["id", "title", "body", "categorys"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]
