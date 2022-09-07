from rest_framework import serializers
from .models import User, Teacher, Student, Group


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'group_name', 'course', 'teacher', 'student')


class GroupTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher

    def to_representation(self, obj):
        match isinstance(obj, Teacher):
            case True:
                serializer = TeacherSerializer(obj)
            case False:
                serializer = GroupSerializer(obj)
            case _:
                raise Exception("Nothing to serialize.")
        return serializer.data