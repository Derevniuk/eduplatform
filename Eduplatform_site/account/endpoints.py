from rest_framework import permissions
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Group, Student, Teacher, User
from .serializers import (
    GroupSerializer,
    StudentSerializer,
    TeacherSerializer,
    UserSerializer,
)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAdminUser]


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAdminUser]


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]


class GroupTeacherViewAPI(ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

    def get_queryset(self):
        teacher = self.kwargs["id"]
        return Group.objects.filter(teacher__in=teacher)
