from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from website.models import Post
from api.serializers import EntrySerializer


class OSSNList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = EntrySerializer


class EntryDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = EntrySerializer
