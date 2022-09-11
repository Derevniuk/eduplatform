from rest_framework import generics, permissions
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


class CourseTopicViewAPI(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()

    def get_queryset(self):
        course = self.kwargs["id"]
        return Topic.objects.filter(course_id=course)


class TopicArticleViewAPI(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def get_queryset(self):
        topic = self.kwargs["id"]
        return Article.objects.filter(topic_id=topic)


class TestQuestionViewAPI(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def get_queryset(self):
        test = self.kwargs["id"]
        return Question.objects.filter(test_id=test)


class QuestionAnswerViewAPI(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

    def get_queryset(self):
        question = self.kwargs["id"]
        return Answer.objects.filter(question_id=question)
