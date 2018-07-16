from django.conf.urls import url

from .views import (
	TweetListAPIView
	# TweetDetailView, 
	# TweetCreateView, 
	# TweetUpdateView, 
	# TweetDeleteView
	)

urlpatterns = [
	url(r'^$', TweetListAPIView.as_view(), name='list'),
]
