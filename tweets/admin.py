from django.contrib import admin

# Register your models here.

from .models import Tweet
from .forms import TweetForm
# admin.site.register(Tweet)

class TweetModelForm(admin.ModelAdmin):
	# form = TweetForm
	class Meta:
		model = Tweet

admin.site.register(Tweet, TweetModelForm)
