import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
# 每个模型被表示为 django.db.models.Model 类的子类

class Question(models.Model):
    question_text = models.CharField(max_length=200)  # char，最长长度为 200
    pub_date = models.DateTimeField('date published')  # date_time，默认值为 date published?

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1) # 时间小于一天


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 外键，
    choice_text = models.CharField(max_length=300)  # char，最长长度为 200
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
