from django.db import models
from django.utils import timezone


class Release(models.Model):
    release_names = models.CharField(max_length=10)


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    ossn = models.CharField(max_length=10)
    release = models.ManyToManyField(Release, blank=True)
    title = models.CharField(max_length=200)
    discussion = models.TextField()
    summary = models.TextField()
    actions = models.TextField()
    contact = models.CharField(max_length=50)
    references = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
