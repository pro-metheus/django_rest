from django.conf.urls import url
from .views import api_handler

urlpatterns=[

url(r'^api/(?P<api_key>[0-9a-f]{32}\Z)',api_handler)
]
