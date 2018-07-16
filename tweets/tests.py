from django.test import TestCase
from .models import Tweet
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your tests here.
User = get_user_model()

class TweetModelTestCase(TestCase):
	def setUp(self):
		test_user = User.objects.create(username="Tester")

	def test_tweet(self):
		obj = Tweet.objects.create(
			user=User.objects.first(),
			content = 'hello there!'
			)
		self.assertTrue(obj.content == "hello there!")
		self.assertTrue(obj.id == 1)
		absolute_url = reverse("tweet:detail", kwargs={'pk':1})
		self.assertEqual(obj.get_absolute_url(), absolute_url)

	def test_update_tweet(self):
		obj2 = Tweet.objects.create(user=User.objects.first(), content = 'hello there!')

		response = self.client.post(
			reverse('tweet:update', kwargs={'pk': obj2.id}),
			{'user': User.objects.first(), 'content': 'Updated content'})

		self.assertEqual(response.status_code, 302)

		Tweet.refresh_form_db()
		self.assertEqual(obj2.content, 'Updated content')

	# def test_tweet_update(self):
	# 	obj2 = Tweet.objects.create(
	# 		user=User.objects.first(),
	# 		content = 'hello there!'
	# 		)
	# 	self.assertTrue(obj2.content == "hello there!")
	# 	obj2 = Tweet.objects.update(
	# 		user=User.objects.first(),
	# 		content = 'Updated content!'
	# 		)
	# 	self.assertTrue(obj2.content == "Updated content")


	def test_tweet_url(self):
		obj = Tweet.objects.create(
			user = User.objects.first(),
			content = 'some random content')
		absolute_url = reverse("tweet:detail", kwargs={'pk': obj.pk})
		self.assertEqual(obj.get_absolute_url(), absolute_url)