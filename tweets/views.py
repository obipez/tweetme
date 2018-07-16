from django.shortcuts import render
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView, 
	UpdateView,
	DeleteView)
from django import forms
from django.forms.utils import ErrorList
from .models import Tweet
from .forms import TweetForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import FormUserNeededMixin, UserMixin
from django.db.models import Q


class TweetListView(ListView):
	template_name = "tweets/list_view.html"
	# queryset = Tweet.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(TweetListView, self).get_context_data(*args, **kwargs)
		context['create_form'] = TweetForm
		context['create_url'] = reverse_lazy("tweet:create")
		return context

	def get_queryset(self, *args, **kwargs):
		qs = Tweet.objects.all()
		print(self.request.GET)
		query = self.request.GET.get("query", None)
		if query is not None:
			print (query)
			qs = qs.filter(Q(content__icontains = query) 
				| Q(user__username__icontains=query))
		# content_query = self.request.GET.get('query')
		# new_content = Tweet.objects.filter(content__icontains = content_query) | Q(user_statswith = self.request.user)
		return qs


class TweetDetailView(DetailView):
	template_name = "tweets/detail_view.html"
	queryset = Tweet.objects.all()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		print(context)
		return context


class TweetCreateView(FormUserNeededMixin, CreateView):
	form_class = TweetForm
	template_name = 'tweets/create_tweet.html'
	# success_url = reverse_lazy("tweet:detail")


class TweetUpdateView(UserMixin, UpdateView):
	queryset = Tweet.objects.all()
	form_class = TweetForm
	template_name = 'tweets/update_tweet.html'
	# success_url = reverse_lazy("tweet:detail")


class TweetDeleteView(LoginRequiredMixin,DeleteView):
	model = Tweet
	success_url = reverse_lazy("tweet:list")
	template_name = 'tweets/delete_tweet.html'
	login_url = reverse_lazy("home")


# Create your views here.
# def tweet_list(request):
# 	queryset = Tweet.objects.all()
# 	for obj in queryset:
# 		print(obj.content)
# 	context ={
# 		"object_list" : queryset,
# 	}
# 	return render(request, "tweets/list_view.html", context)queryset = 