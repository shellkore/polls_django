import datetime
from django.test import TestCase
from django.utils import timezone

from .models import Question

# Create your tests here.

class QuestionModelTests(TestCase):
	def test_was_published_recently_for_future_date(self):
		time= timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertIs(future_question.was_published_recently(),False)

	def test_was_published_recently_for_past_date(self):
		time= timezone.now() - datetime.timedelta(days=1,seconds=1)
		past_question = Question(pub_date=time)
		self.assertIs(past_question.was_published_recently(),False)

	def test_was_published_recently_for_recent_date(self):
		time= timezone.now() - datetime.timedelta(hours=23,minutes=59,seconds=59)
		recent_question = Question(pub_date=time)
		self.assertIs(recent_question.was_published_recently(),True)