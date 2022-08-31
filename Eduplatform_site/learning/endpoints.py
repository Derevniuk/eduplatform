from rest_framework.viewsets import ModelViewSet

from .models import Answer, Article, Attempt, Course, Question, Test, Topic
from .serializers import (
    AnswerSerializer,
    ArticleSerializer,
    AttemptSerializer,
    CourseSerializer,
    QuestionSerializer,
    TestSerializer,
    TopicSerializer,
)


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class TopicViewSet(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class TestViewSet(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AttemptViewSet(ModelViewSet):
    queryset = Attempt.objects.all()
    serializer_class = AttemptSerializer
