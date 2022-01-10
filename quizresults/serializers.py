from rest_framework import serializers
from .models import Results,QuizUser


class QuizUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuizUser
        fields = [
            'name',
        ]

class ResultSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = Results
        fields = [
            'user_id',
            'answer',
        ]