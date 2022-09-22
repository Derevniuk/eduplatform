from rest_framework import serializers

from .models import Group, Student, Teacher, User
from learning.serializers import CourseSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","first_name","last_name","email","last_login",)
        extra_kwargs = {
            "password": {"write_only": True},
        }


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Teacher
        fields = ('id','user')


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Student
        fields = ('id','user')


class GroupSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    teacher = TeacherSerializer()
    student = StudentSerializer(many=True)
    class Meta:
        model = Group
        fields = ("id", "group_name", "course", "teacher", "student")


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

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password", "first_name", "last_name")
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
