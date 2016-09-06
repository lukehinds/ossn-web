from __future__ import unicode_literals
from django import template
from website.models import Post

register = template.Library()


def decode_release(ingredients):
    """
    Decode pizza pie toppings
    """
    decoder = dict(Post.RELEASE_CHOICES)
    decoded = [decoder[t] for t in ingredients]
    decoded.sort()
    return ', '.join(decoded)

register.filter('decode_release', decode_release)
