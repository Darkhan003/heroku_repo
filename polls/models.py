from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime
from django.utils import timezone
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

class Post(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, validators=[alphanumeric])
    surname = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    student_id = models.CharField(max_length=255, default=' ')
    email = models.CharField(max_length=255, default=' ')
    password = models.TextField(max_length=255, default=' ')
    header_image = models.ImageField(null=True,  upload_to='images/')



    def __str__(self):
        return self.name + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Kazakh(models.Model):
    kazakh_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.kazakh_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text