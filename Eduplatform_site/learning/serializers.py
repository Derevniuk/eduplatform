from rest_framework import serializers
from .models import (Answer,
                     Article,
                     Attempt,
                     Course,
                     Question,
                     Test,
                     Topic,
                     Teacher,
                     Student,
                     Group,
                     Photo,
                     )

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id','user','photo')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','user','photo')


class GroupTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher

    def to_representation(self, obj):
        if obj:
            if isinstance(obj, Teacher):
                serializer = TeacherSerializer(obj)
            else:
                serializer = GroupSerializer(obj)
        else:
            raise Exception("Nothing to serialize.")
        return serializer.data


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ("id", "topic", "creator", "title", "description")


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("id", "test", "text")


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ("id", "question", "text")


class AttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attempt
        fields = "__all__"

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "group_name", "course", "teacher", "student")

class GroupStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupSerializer

    def to_representation(self, obj):
        if obj:
            if isinstance(obj, Group):
                serializer = GroupSerializer(obj)
            else:
                serializer = StudentSerializer(obj)
        else:
            raise Exception("Nothing to serialize.")
        return serializer.data