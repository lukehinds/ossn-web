from django.conf.urls import url
from api.views import OSSNList, EntryDetail


urlpatterns = [
    url(r'^api/1.0/$', OSSNList.as_view()),
    url(r'^entry/(?P<pk>[0-9]+)/$', EntryDetail.as_view()),
]
