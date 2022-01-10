from django.urls import path
from .views import QuizUserView,ResultView

app_name='quizresults'

urlpatterns = [
    path('set_quizuser', QuizUserView.as_view(), name='set_quizuser'),
    path('post_result', ResultView.as_view(), name='post_result' ),
]