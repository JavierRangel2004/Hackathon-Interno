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

from django.contrib.auth import get_user_model

UserModel = get_user_model()

class CompanyRegistrationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ('email', 'username', 'password', 'user')

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            is_company=True
        )
        company = Company.objects.create(user=user)
        return company

class AdvisorRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ('email', 'username', 'password', 'is_advisor')

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            is_advisor=True
        )
        return user
