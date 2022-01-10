from django.db import models
from quiz.models import Answer
# Create your models here.

class QuizUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name + "(" + self.user_id+ + ")"

class Result(models.Model):
    user = models.ForeignKey(QuizUser, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
