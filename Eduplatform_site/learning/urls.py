from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .endpoints import (
    AnswerViewSet,
    ArticleViewSet,
    AttemptViewSet,
    CourseViewSet,
    QuestionViewSet,
    TestViewSet,
    TopicViewSet,
)

router = DefaultRouter()
router.register("courses", CourseViewSet)
router.register("topics", TopicViewSet)
router.register("articles", ArticleViewSet)
router.register("tests", TestViewSet)
router.register("questions", QuestionViewSet)
router.register("answers", AnswerViewSet)
router.register("attempts", AttemptViewSet)


urlpatterns = [path("", include(router.urls))]
