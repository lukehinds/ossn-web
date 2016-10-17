from rest_framework import serializers
from website.models import Post


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('ossn', 'releases', 'title', 'discussion', 'summary', 'actions', 'contact',
                  'references', 'created_date', 'published_date')
