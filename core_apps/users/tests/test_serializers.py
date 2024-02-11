import pytest
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from core_apps.users.serializers import UserSerializer, CustomRegisterSerializer


User = get_user_model()


@pytest.mark.django_db
def test_user_serializer(normal_user):
    serializer = UserSerializer(normal_user)
    assert "id" in serializer.data
    assert "email" in serializer.data
    assert "first_name" in serializer.data
    assert "last_name" in serializer.data
    assert "gender" in serializer.data
    assert "phone_number" in serializer.data
    assert "profile_photo" in serializer.data
    assert "country" in serializer.data
    assert "city" in serializer.data


@pytest.mark.django_db
def test_to_representation_normal_user(normal_user):
    serializer = UserSerializer(normal_user)
    serializer_data = serializer.data
    assert "admin" not in serializer_data


@pytest.mark.django_db
def test_to_representation_super_user(super_user):
    serializer = UserSerializer(super_user)
    serializer_data = serializer.data
    assert "admin" in serializer_data
    assert serializer_data["admin"] is True


@pytest.mark.django_db
def test_custom_register_serializer(mock_request):
    valid_data = {
        "email": "admin@example.com",
        "first_name": "admin",
        "last_name": "admin",
        "password1": "adminadmin",
        "password2": "adminadmin",
    }
    serializer = CustomRegisterSerializer(data=valid_data)
    assert serializer.is_valid()

    user = serializer.save(mock_request)
    assert user.email == valid_data["email"]
    assert user.first_name == valid_data["first_name"]
    assert user.last_name == valid_data["last_name"]

    invalid_data = {
        "email": "admin@example.com",
        "first_name": "admin",
        "last_name": "admin",
        "password1": "adminadmin",
        "password2": "wrongadmin",
    }

    serializer = CustomRegisterSerializer(data=invalid_data)
    with pytest.raises(ValidationError):
        serializer.is_valid(raise_exception=True)
