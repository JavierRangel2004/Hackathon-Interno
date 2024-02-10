from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Certification, Company, Advisor, ForumPost, User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

UserModel = get_user_model()

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = '__all__'

class ForumPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumPost
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_advisor', 'is_company']

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user
'''class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    sustainability_score = models.IntegerField(default=0)
    improvements_needed = models.TextField()
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    ranking = models.IntegerField(default=0)
    certifications = models.ManyToManyField(Certification, blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    number_of_employees = models.IntegerField(default=0)
    sector = models.CharField(max_length=255, blank=True, null=True)'''

'''test post:
{
  "user": {
    "username": "companyUsername",
    "email": "company@example.com",
    "password": "securepassword123"
  },
  "name": "Company Name",
  "phone": "123-456-7890",
  "address": "123 Business St., Business City",
  "number_of_employees": 50,
  "sector": "Technology"
}


'''
class CompanyRegistrationSerializer(serializers.Serializer):
    user = UserRegistrationSerializer()
    name = serializers.CharField()
    phone = serializers.CharField()
    # Add any other company specific fields here
    email = serializers.EmailField()
    address = serializers.CharField(allow_blank=True, allow_null=True)
    number_of_employees = serializers.IntegerField()
    sector = serializers.CharField(allow_blank=True, allow_null=True)
    # Include logo if uploaded

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserRegistrationSerializer.create(UserRegistrationSerializer(), validated_data=user_data)
        user.is_company = True
        user.save()
        company = Company.objects.create(user=user, **validated_data)
        return company

class AdvisorRegistrationSerializer(serializers.Serializer):
    user = UserRegistrationSerializer()
    name = serializers.CharField()
    phone = serializers.CharField()
    specialty = serializers.CharField()
    sponsored = serializers.BooleanField(default=False)
    email = serializers.EmailField()
    # Include profile_picture if required

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserRegistrationSerializer.create(UserRegistrationSerializer(), validated_data=user_data)
        user.is_advisor = True
        user.save()
        advisor = Advisor.objects.create(user=user, **validated_data)
        return advisor

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['is_advisor'] = user.is_advisor
        token['is_company'] = user.is_company
        return token
