from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Topic(models.Model):
    """A topic the user is interested in."""
    # text ve date_added adında veritabanında 2 sütun oluşturacağız
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the topic."""
        return self.text

    def delete_topic(self):
        """Delete the topic"""
        self.delete()


class Entry(models.Model):
    """Something specific learned about a topic."""
    # ForeignKey field'ı "çoktan-bire" ilişkiyi temsil eder. Her Entry bir Topic ile ilişkilidir.
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Entries"

    def __str__(self):
        """Return a string representation of the model"""
        return f"{self.text[:50]}..."

    def delete_entry(self):
        """Delete the entry"""
        self.delete()

