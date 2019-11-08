from abc import ABC

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    confirmPassword = serializers.CharField(style={'input_type': 'password'}, max_length=90, write_only=True)
    password = serializers.CharField(style={'input_type': 'password'}, max_length=90, write_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "password",
            "confirmPassword"
        ]

        read_only_fields = ("id",)

    def validate(self, attrs):
        requestMethod = self.context.get("request").method.lower()
        if requestMethod == "post":
            if attrs.get("password") != attrs.pop("confirmPassword"):
                raise ValidationError("passwords do not match")
            return attrs
        return attrs

    def create(self, validated_data):
        instance = super().create(validated_data)
        print(validated_data.get("password"))
        instance.set_password(validated_data.pop("password"))
        instance.save()
        return instance


class UserPasswordChangeSerializer(serializers.Serializer):
    currentPassword = serializers.CharField(style={'input_type': 'password'}, max_length=90)
    password = serializers.CharField(style={'input_type': 'password'}, max_length=90)
    confirmPassword = serializers.CharField(style={'input_type': 'password'}, max_length=90)

    def validate(self, attrs):
        print(self.context)
        user = self.context.get("request").user
        if not user.check_password(attrs.get("currentPassword")):
            raise ValidationError("wrong password")
        return attrs
