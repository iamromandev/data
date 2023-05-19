import uuid

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from taggit.models import (
    GenericUUIDTaggedItemBase,
    TaggedItemBase,
)
from django_softdelete.models import SoftDeleteModel


class Tag(GenericUUIDTaggedItemBase, TaggedItemBase):
    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Source(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    type = models.CharField(max_length=32, blank=False, null=False)
    subtype = models.CharField(max_length=32, blank=False, null=False)
    source = models.CharField(max_length=256, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[Source: {self.type}, {self.subtype}, {self.source}]'

    class Meta:
        ordering = ['source']


class Store(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    ref = models.UUIDField(editable=False, default=uuid.uuid4)
    type = models.CharField(max_length=32, blank=False, null=False)
    subtype = models.CharField(max_length=32, blank=False, null=False)
    state = models.CharField(max_length=32, blank=False, null=False)
    extra = models.CharField(max_length=32, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[Store: {self.type}, {self.subtype}, {self.state}]'

    class Meta:
        ordering = ['type', 'subtype']
        unique_together = [['ref', 'type', 'subtype']]

    def is_expired(self, delay):
        return int(timezone.now().timestamp()) - int(self.updated_at.timestamp()) > delay


class Language(SoftDeleteModel):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    source = models.ForeignKey(Source, related_name='languages', on_delete=models.DO_NOTHING)
    code = models.CharField(max_length=8, blank=False, null=False)
    name = models.CharField(max_length=32, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'[Language: {self.source}, {self.code}, {self.name}]'