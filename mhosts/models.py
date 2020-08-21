from django.db import models


class Host_type(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Host(models.Model):
    """Something specific learned about a topic."""
    host_type = models.ForeignKey(Host_type)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    host_name = models.CharField(max_length=200)

    host_ip = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'hosts'

    def __str__(self):
        """Return a string representation of the model."""
        return self.host_name

