from django.db import models
from quiz.models import Answer
# Create your models here.

class QuizUser(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Results(models.Model):
    user_id = models.ForeignKey(QuizUser, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    def __str__(self):
        return self.answer