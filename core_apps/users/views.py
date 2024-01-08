# pylint: disable = C0115

from rest_framework.generics import RetrieveUpdateAPIView  # type: ignore
from rest_framework.permissions import IsAuthenticated  # type: ignore
from django.contrib.auth import get_user_model  # type: ignore
from .serializers import UserSerializer


class CustomUserDetailsView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = IsAuthenticated

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        return get_user_model().objects.none()
