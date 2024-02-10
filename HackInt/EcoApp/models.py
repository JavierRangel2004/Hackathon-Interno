# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_advisor = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)

class Sector(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Specialty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company')
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    number_of_employees = models.IntegerField(default=0, blank=True, null=True)
    sectors = models.ManyToManyField(Sector, blank=True, related_name='companies')
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    sustainability_score = models.IntegerField(default=0, blank=True, null=True)
    ranking = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.user.username

class Advisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='advisor')
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    specialties = models.ManyToManyField(Specialty, blank=True, related_name='advisors')
    profile_picture = models.ImageField(upload_to='advisor_profile_pictures/', blank=True, null=True)
    sponsored = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Certification(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    requirements = models.TextField()
    benefits = models.TextField()
    image = models.ImageField(upload_to='certification_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class ForumPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='forum_posts')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
