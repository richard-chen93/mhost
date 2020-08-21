from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)
    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Host(models.Model):
    """Something specific learned about a topic."""
    group = models.ForeignKey(Group)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    host_name = models.CharField(max_length=200)

    host_ip = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'hosts'

    def __str__(self):
        """Return a string representation of the model."""
        return self.host_name

