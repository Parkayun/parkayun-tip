from django.db import models


class CascadeProtectQuerySet(models.query.QuerySet):

    def delete(self):
        self.update(is_active=False)


class CascadeProtectManager(models.Manager):

    def __init__(self, *args, **kwargs):
        super(CascadeProtectManager, self).__init__(*args, **kwargs)

    def get_query_set(self):
        return CascadeProtectQuerySet(self.model, using=self._db)

    def _all(self):
        return super(CascadeProtectManager, self).all()

    def all(self):
        return super(CascadeProtectManager, self).filter(is_active=True)

    def _get(self, *args, **kwargs):
        return super(CascadeProtectManager, self).get(*args, **kwargs)

    def get(self, *args, **kwargs):
        kwargs['is_active'] = True
        return super(CascadeProtectManager, self).get(*args, **kwargs)

    def _filter(self, *args, **kwargs):
        return super(CascadeProtectManager, self).filter(*args, **kwargs)

    def filter(self, *args, **kwargs):
        kwargs['is_active'] = True
        return super(CascadeProtectManager, self).filter(*args, **kwargs)


class CascadeProtectedModel(models.Model):

    objects = CascadeProtectManager()

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()

    class Meta:
        abstract = True


class SomeModel(CascadeProtectedModel):

    some_field = models.CharField(max_length=10)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
