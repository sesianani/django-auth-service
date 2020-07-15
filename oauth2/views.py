from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_401_UNAUTHORIZED
from rest_framework import serializers
from .serializers import LoginSerializer
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render


class AuthenticationView(APIView):
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        username = request.data["username"]
        password = request.data["password"]

        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return Response({
                    "alert": "success",
                    "message": "User authentication was successful!",
                    "data": {}
                }, status=HTTP_200_OK)
            else:
                return Response({
                    "alert": "error",
                    "message": "User authentication failed! Please try again.",
                    "data": {}
                }, status=HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def get(self, request):
        logout(request)
        return Response({
            "alert": "success",
            "message": "User logged out successfully!",
            "data": {}
        }, status=HTTP_200_OK)
