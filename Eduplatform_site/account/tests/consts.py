from account import models
from account.annotations import UserAnnotation as User

USER_DATA = {"email": "test_user@test.ru", "password": "123456", "first_name": "Test", "last_name": "Test"}


def create_user() -> User:
    user = models.User.objects.create(password="123456", email="test_user@test.ru", first_name="Test", last_name="Test")
    return user
