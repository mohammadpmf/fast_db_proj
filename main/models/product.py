from django.db import models

from main.models import GBSoftDeleteModel, TimeStampMixin
from main.models.category import Category


class Product(TimeStampMixin, GBSoftDeleteModel):
    category = models.ForeignKey(
        to=Category, on_delete=models.PROTECT, null=True, blank=True
    )
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000, null=True, blank=True)
    price = models.FloatField()
    extra_info = models.TextField(null=True, blank=True)

    def __str__(self):
        if self.category:
            return f"{self.category}: {self.title}"
        return f"{self.title}"
