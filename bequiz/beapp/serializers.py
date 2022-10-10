from rest_framework.serializers import ModelSerializer

from .models import Question, Quiz,Choice,Answer


class GetAllQuizSerializer(ModelSerializer):
    """
    This serializer for getting all the quizzed
    """
    class Meta:
        model = Quiz
        fields = "__all__"


class GetQuestionSerializer(ModelSerializer):
    """
    This serializer for getting all the questions
    """
    class Meta:
        model = Question
        fields = "__all__"

class GetChoiceSerializer(ModelSerializer):
    """
    This serializer for getting all the choices
    """
    class Meta:
        model = Choice
        fields = "__all__"

class GetAnswerSerializer(ModelSerializer):
    """
    This serializer for getting all the answers
    """
    class Meta:
        model = Answer
        fields = "__all__"