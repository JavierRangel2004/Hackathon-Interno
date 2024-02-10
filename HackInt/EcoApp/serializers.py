# serializers.py
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Company, Advisor, Sector, Specialty, Certification, ForumPost
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


UserModel = get_user_model()

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields= '__all__'

class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = '__all__'

class AdvisorRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['is_advisor'] = True
        user = UserModel.objects.create_user(**validated_data)
        return user

class CompanyRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['is_company'] = True
        user = UserModel.objects.create_user(**validated_data)
        return user

class CompanyProfileUpdateSerializer(serializers.ModelSerializer):
    sectors = serializers.PrimaryKeyRelatedField(many=True, queryset=Sector.objects.all(), required=False)

    class Meta:
        model = Company
        fields = ['name', 'email', 'phone', 'address', 'number_of_employees', 'sectors', 'logo']
        extra_kwargs = {field: {'required': False} for field in fields}

    def update(self, instance, validated_data):
        instance.sectors.set(validated_data.get('sectors', instance.sectors.all()))
        return super().update(instance, validated_data)

class AdvisorProfileUpdateSerializer(serializers.ModelSerializer):
    specialties = serializers.PrimaryKeyRelatedField(many=True, queryset=Specialty.objects.all(), required=False)

    class Meta:
        model = Advisor
        fields = ['name', 'email', 'phone', 'specialties', 'profile_picture']
        extra_kwargs = {field: {'required': False} for field in fields}

    def update(self, instance, validated_data):
        instance.specialties.set(validated_data.get('specialties', instance.specialties.all()))
        return super().update(instance, validated_data)

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = '__all__'

class ForumPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumPost
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = '__all__'

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['is_advisor'] = user.is_advisor
        token['is_company'] = user.is_company

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        data['is_advisor'] = self.user.is_advisor
        data['is_company'] = self.user.is_company

        return data

#add certification registration serializer

class CertificationRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = ['name', 'description', 'requirements', 'benefits', 'image']
        extra_kwargs = {'image': {'required': False}}

    def create(self, validated_data):
        certification = Certification.objects.create(**validated_data)
        return certification