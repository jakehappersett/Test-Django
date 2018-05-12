import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    '''
    Question set for poll app
    '''
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    '''
    Choice set for polls app
    '''
    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

