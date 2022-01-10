from rest_framework import generics
from rest_framework.response import Response
from .models import Quizzes, Question
from .serializers import QuizSerializer, QuestionSerializer
from rest_framework.views import APIView

class Quiz(generics.ListAPIView):

    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()


class QuizQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        quiz = Question.objects.filter(quiz__title=kwargs['topic'])
        serializer = QuestionSerializer(quiz, many=True)
        return Response(serializer.data)