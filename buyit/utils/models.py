import auto_prefetch
from django.db import models
from buyit.utils.managers import VisibleManager

class TimeBasedModel(auto_prefetch.Model):
    visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(auto_prefetch.Model.Meta):
        abstract = True

    objects = auto_prefetch.Manager()
    items = VisibleManager()


class NamedTimeBasedModel(TimeBasedModel):
    name = models.CharField(max_length=200, blank=True, null=True)

    class Meta(auto_prefetch.Model.Meta):
        abstract = True
        ordering = ["name", "created_at"]

    def __str__(self):
        return self.name

    def title(self):
        """alias for `name` field"""
        return self.name

