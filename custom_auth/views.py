from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LoginSerializer, ResgisterSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class ResgisterAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = ResgisterSerializer(data=data)

        if not serializer.is_valid():
            return Response({"status": False, "data": serializer.errors})
        serializer.save()
        return Response(serializer.data)


class LoginAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if not serializer.is_valid():
            return Response(
                {
                    "status": status.HTTP_404_NOT_FOUND,
                    "data": serializer.errors,
                }
            )
        username = serializer.data["username"]
        password = serializer.data["password"]
        user_obj = authenticate(username=username, password=password)
        print(username, password)
        if user_obj:
            token, created = Token.objects.get_or_create(user=user_obj)
            return Response(
                {
                    "status": status.HTTP_200_OK,
                    "data": {"token": token.key},
                }
            )

        return Response(
            {
                "status": status.HTTP_404_NOT_FOUND,
                "data": {"message": "Invalid credentials"},
            }
        )
