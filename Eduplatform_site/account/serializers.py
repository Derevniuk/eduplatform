from rest_framework import serializers

from .models import Group, Student, Teacher, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            "password": {"write_only": True},
        }


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
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
