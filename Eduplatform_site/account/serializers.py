
from rest_framework import serializers
from .models import User,Teacher,Student,Group



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name','email']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id','user')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','user','rating')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'group_name', 'course','teacher','student')

