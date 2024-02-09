from rest_framework import serializers
from .models import Certification, Company, Supplier, ForumPost, User
#a serializer is a class that converts complex data types, such as querysets and model instances, to native Python datatypes that can then be easily rendered into JSON, XML or other content types.

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class ForumPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumPost
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_advisor', 'is_company']
