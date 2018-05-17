
from django.conf.urls import url
from django.urls import path, include

#TOKEN AUTH ENDPOINT
from rest_framework.authtoken.views import obtain_auth_token


from .views import (
    PartyCreateAPIView,
    # UserAPIViewset,
    PartyListAPIView,
    PartyDetailByIdAPIView,
    PartyEditAPIView,
    PartyDeleteAPIView,
)
urlpatterns = [
    #url('',include(router.urls)),
    url(r'^$', PartyListAPIView.as_view(), name='list'),
    url(r'^create/$', PartyCreateAPIView.as_view(), name='create'),
    
    url(r'(?P<id>\d+)/edit/$', PartyEditAPIView.as_view(), name = 'edit'),
    url(r'(?P<id>\d+)/delete/$', PartyDeleteAPIView.as_view(), name = 'delete'),
    url(r'auth-token/$', obtain_auth_token, name='token'),
    url(r'(?P<id>\d+)/$', PartyDetailByIdAPIView.as_view(), name = 'detail-id'),
   
]
