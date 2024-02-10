# views.py
from django.shortcuts import get_object_or_404
from rest_framework import status, views, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Company, Advisor , Certification, ForumPost
from .serializers import (
    AdvisorRegistrationSerializer, CompanyRegistrationSerializer, CompanyProfileUpdateSerializer,
    AdvisorProfileUpdateSerializer, CertificationSerializer, ForumPostSerializer,
    CompanySerializer, AdvisorSerializer, CustomTokenObtainPairSerializer
)
from rest_framework_simplejwt.views import TokenObtainPairView

class AdvisorRegistrationView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = AdvisorRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            Advisor.objects.create(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompanyRegistrationView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = CompanyRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            Company.objects.create(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompanyProfileUpdateView(views.APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        user = request.user
        company = get_object_or_404(Company, user=user)
        serializer = CompanyProfileUpdateSerializer(company, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdvisorProfileUpdateView(views.APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        user = request.user
        advisor = get_object_or_404(Advisor, user=user)
        serializer = AdvisorProfileUpdateSerializer(advisor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class CertificationViewSet(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer

class ForumPostViewSet(viewsets.ModelViewSet):
    queryset = ForumPost.objects.all()
    serializer_class = ForumPostSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class AdvisorViewSet(viewsets.ModelViewSet):
    queryset = Advisor.objects.all()
    serializer_class = AdvisorSerializer
