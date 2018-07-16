from django.shortcuts import render
# from .forms import TweetForm

def home(request):
	return render(request, "homepage.html", {})