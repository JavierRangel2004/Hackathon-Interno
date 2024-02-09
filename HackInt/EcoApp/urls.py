from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CertificationViewSet, CompanyViewSet, SupplierViewSet, ForumPostViewSet, UserViewSet
from .views import CompanyRegistrationView, AdvisorRegistrationView



router = DefaultRouter()
router.register(r'certifications', CertificationViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'forumposts', ForumPostViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('register/company/', CompanyRegistrationView.as_view(), name='register_company'),
    path('register/advisor/', AdvisorRegistrationView.as_view(), name='register_advisor'),
]
