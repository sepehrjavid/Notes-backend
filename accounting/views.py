import requests
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounting.serializers import UserSerializer, UserPasswordChangeSerializer


class UserSignUpView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class UserPasswordChangeView(APIView):
    serializer_class = UserPasswordChangeSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = self.request.user
        serializer = self.serializer_class(data=request.data, context={"request": self.request})
        if serializer.is_valid():
            user.set_password(serializer.validated_data.get("password"))
            user.save()
            return Response({"message": "password changed successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
