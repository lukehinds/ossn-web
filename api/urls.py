from django.conf.urls import url
from api.views import EntryList, EntryDetail


urlpatterns = [
    url(r'^entries/$', EntryList.as_view()),
    url(r'^entry/(?P<pk>[0-9]+)/$', EntryDetail.as_view()),
]
