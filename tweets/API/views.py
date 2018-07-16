from rest_framework import generics
from tweets.models import Tweet
from .serializers import ModelTweetSerializer

class TweetListAPIView(generics.ListAPIView):
	serializer_class = ModelTweetSerializer
	queryset = Tweet.objects.all()