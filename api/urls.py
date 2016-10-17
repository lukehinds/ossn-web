from django.conf.urls import url
from api.views import OSSNList


urlpatterns = [
    url(r'^api/1.0/$', OSSNList.as_view()),
]
