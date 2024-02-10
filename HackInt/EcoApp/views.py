from rest_framework import viewsets, status, views
from rest_framework.response import Response
from .models import Certification, Company, Advisor, ForumPost
from .serializers import (
    CertificationSerializer, CompanySerializer, AdvisorSerializer,
    ForumPostSerializer, CompanyRegistrationSerializer, 
    AdvisorRegistrationSerializer, CustomTokenObtainPairSerializer
)
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.views import View


# Assuming your CustomTokenObtainPairView is correctly configured as per previous discussions
class Alive(View):
    def get(self, request):
        return Response({"status": "alive"}, status=status.HTTP_200_OK)

# ViewSets for Certification, Company, Advisor, and ForumPost
class CertificationViewSet(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class AdvisorViewSet(viewsets.ModelViewSet):
    queryset = Advisor.objects.all()
    serializer_class = AdvisorSerializer

class ForumPostViewSet(viewsets.ModelViewSet):
    queryset = ForumPost.objects.all()
    serializer_class = ForumPostSerializer

# Registration Views
class CompanyRegistrationView(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = CompanyRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            company = serializer.save()
            return Response(CompanySerializer(company).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdvisorRegistrationView(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = AdvisorRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            advisor = serializer.save()
            return Response(AdvisorSerializer(advisor).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
