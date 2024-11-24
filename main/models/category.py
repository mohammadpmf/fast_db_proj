from django.db import models

from main.models import GBSoftDeleteModel, TimeStampMixin


class Category(TimeStampMixin, GBSoftDeleteModel):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000, null=True, blank=True)
    parent = models.ForeignKey(to='self', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        titles = []
        current_category = self
        while current_category:
            titles.append(current_category.title)
            current_category = current_category.parent
        return " >> ".join(reversed(titles))
