from django.core.exceptions import ValidationError
from rest_framework import serializers

from category.models import Category
from note.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = [
            "id",
            "title",
            "body",
            "isImportant",
            "isPerformed",
            "date"
        ]

        read_only_fields = ("id", "date",)

    def validate(self, attrs):
        if self.context.get("request").method.lower() == "post":
            category = Category.objects.filter(id=self.context.get("view").kwargs.get("category_pk"))
            if not category.exists():
                raise ValidationError("category does not exist")
            attrs["category"] = category.first()
        return attrs
