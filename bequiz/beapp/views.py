from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Question, Quiz ,Choice,Answer

from .serializers import GetAllQuizSerializer, GetQuestionSerializer,GetChoiceSerializer,GetAnswerSerializer
class GetAllQuizView(ListAPIView, GenericViewSet):
    """
    This view is to get all quizes
    """
    permission_classes = [IsAuthenticated,]
    serializer_class = GetAllQuizSerializer
    queryset = Quiz.objects.all()

class GetQuestionsForQuizView(ListAPIView, GenericViewSet):
    """
    Get all the questions for particular quiz
    """
    permission_classes = [IsAuthenticated,]
    serializer_class = GetQuestionSerializer
    queryset = Question.objects.all()

    def get_queryset(self):
        return Question.objects.filter(quiz = Quiz.objects.get(pk = self.kwargs['qid']))

class GetChoicesForQuizView(ListAPIView, GenericViewSet):
    """
    Get all choices for particular question
    """
    permission_classes = [IsAuthenticated,]
    serializer_class = GetChoiceSerializer
    queryset = Choice.objects.all()

class GetAnswerForQuizView(RetrieveAPIView, GenericViewSet):
    """
    Get the answer for particular question
    """
    permission_classes = [IsAuthenticated,]
    serializer_class = GetAnswerSerializer
    queryset = Answer.objects.all()






# Create your views here.


# Create your views here.
