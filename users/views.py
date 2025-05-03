from django.shortcuts import render
from rest_framework import generics, permissions
# from rest_framework.response import Response
# from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer, UserSerializer, EmployerSerializer
from .models import User, Employer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]


class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user
    

class EmployerListView(generics.ListCreateAPIView):
    serializer_class = EmployerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Employer.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EmployerDetailUsingIdView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Employer.objects.filter(user=self.request.user)