from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    """A host group belongs to a user."""
    text = models.CharField(max_length=100)

    os_type = models.CharField(max_length=20, default="windows")

    # date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        """Return a string representation of the model."""
        # return self.text + r'(' + self.os_type + r')'
        return self.text


class Host(models.Model):
    """a host that belongs to a group."""
    group = models.ForeignKey(Group)
    # text = models.TextField()
    # date_added = models.DateTimeField(auto_now_add=True)

    host_name = models.CharField(max_length=50)
    host_ip = models.GenericIPAddressField()

    user_name = models.CharField(max_length=50)
    user_pass = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'hosts'

    def __str__(self):
        """Return a string representation of the model."""
        return self.host_name