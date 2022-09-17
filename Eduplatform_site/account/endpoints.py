from rest_framework import mixins, permissions, status
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .models import Group, Student, Teacher, User
from .serializers import (
    GroupSerializer,
    RegisterSerializer,
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


class RegisterViewApi(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list_user(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


# class LoginViewApi(APIView):
#     serializer_class = LoginSerializer
#     permission_classes = [permissions.AllowAny]
#
#     def post(self, request):
#         user = request.data.get('user', {})
#         serializer = self.serializer_class(data=user)
#         serializer.is_valid(raise_exception=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def list_user(self, request, pk=None):
#         queryset = User.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
