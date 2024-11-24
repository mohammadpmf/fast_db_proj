from django.db import models
from django_softdelete.models import SoftDeleteModel


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class GBSoftDeleteModel(SoftDeleteModel):
    class Meta:
        abstract = True

    deleted_at = models.DateTimeField(blank=True, null=True, db_index=True)


from . import product
from . import category