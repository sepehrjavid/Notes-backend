from django.db import models


class Note(models.Model):
    category = models.ForeignKey("category.Category", on_delete=models.CASCADE, related_name="notes")
    title = models.CharField(max_length=20)
    body = models.TextField(blank=True)
    isImportant = models.BooleanField(default=False)
    isPerformed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
