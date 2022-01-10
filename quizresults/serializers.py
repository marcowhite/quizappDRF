from rest_framework import serializers
from .models import Result,QuizUser
from quiz.serializers import AnswerSerializer


class QuizUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuizUser
        fields = [
            'name',
        ]

class ResultSerializer(serializers.HyperlinkedModelSerializer):

    user = QuizUserSerializer(read_only=True)
    answer = AnswerSerializer(read_only=True)

    class Meta:

        model = Result
        fields = [
            'user',
            'answer',
        ]