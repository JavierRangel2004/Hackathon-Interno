from rest_framework import viewsets
from .models import Certification, Company, Supplier, ForumPost, User
from .serializers import CertificationSerializer, CompanySerializer, SupplierSerializer, ForumPostSerializer, UserSerializer

class CertificationViewSet(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class ForumPostViewSet(viewsets.ModelViewSet):
    queryset = ForumPost.objects.all()
    serializer_class = ForumPostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

from rest_framework import status, views
from rest_framework.response import Response
from .serializers import CompanyRegistrationSerializer, AdvisorRegistrationSerializer

class CompanyRegistrationView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = CompanyRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdvisorRegistrationView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = AdvisorRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
