from django.db import models
import uuid


class BaseModelManager(models.Manager):
    def get_queryset(self):
        return super(BaseModelManager, self).get_queryset().filter()


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    is_deleted = models.BooleanField(default=False, db_index=True)

    objects = BaseModelManager()

    class Meta:
        get_latest_by = "updated_at"
        abstract = True


class PosBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    id = models.CharField(max_length=150, primary_key=True)
    is_deleted = models.BooleanField(default=False, db_index=True)

    objects = BaseModelManager()

    class Meta:
        get_latest_by = "updated_at"
        abstract = True


class ComBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    meta = models.JSONField(null=True, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True)
    is_deleted = models.BooleanField(default=False, db_index=True)
    objects = BaseModelManager()

    class Meta:
        get_latest_by = "updated_at"
        abstract = True
