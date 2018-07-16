from django.conf.urls import url

from .views import (
	TweetListView, 
	TweetDetailView, 
	TweetCreateView, 
	TweetUpdateView, 
	TweetDeleteView)

urlpatterns = [
    url(r'^$', TweetListView.as_view(), name='list'), # localhost:4000/tweet/
    url(r'^create/$', TweetCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'), # localhost:4000/tweet/id_of_tweet
]
