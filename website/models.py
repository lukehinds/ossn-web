from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.utils.encoding import (
    force_text, python_2_unicode_compatible)
from django.utils.translation import ugettext_lazy as _
from select_multiple_field.models import SelectMultipleField


class Post(models.Model):
    JUNO = 'juno'
    KILO = 'kilo'
    LIBERTY = 'liberty'
    RELEASE_CHOICES = (
        (JUNO, 'Juno'),
        (KILO, 'Kilo'),
        (LIBERTY, 'Liberty'),
    )
    releases = SelectMultipleField(
        max_length=50,
        choices=RELEASE_CHOICES,
        default='liberty'
    )
    author = models.ForeignKey('auth.User')
    ossn = models.CharField(max_length=10)
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
        return "pk=%s" % force_text(self.pk)

    def get_releases(self):
        if self.releases:
            keys_choices = self.toppings
            return '%s' % (', '.join(filter(bool, keys_choices)))
    get_releases.short_description = _('Releases')

    def get_absolute_url(self):
        return reverse('Post:detail', args=[self.pk])


def show_release(ingredient):
    """
    Decode release to full name
    """
    decoder = dict(Post.RELEASE_CHOICES)
    return force_text(decoder[ingredient])
