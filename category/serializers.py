from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
        ]

        read_only_fields = ("id",)

    def validate(self, attrs):
        request = self.context.get("request")
        if request is None:
            raise ValidationError("request parameter not included")
        attrs["user"] = request.user
        return attrs
