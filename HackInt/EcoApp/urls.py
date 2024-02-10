from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    CertificationViewSet, CompanyViewSet, AdvisorViewSet, ForumPostViewSet,
    CompanyRegistrationView, AdvisorRegistrationView, CustomTokenObtainPairView
)

router = DefaultRouter()
router.register(r'certifications', CertificationViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'advisors', AdvisorViewSet)
router.register(r'forumposts', ForumPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/company/', CompanyRegistrationView.as_view(), name='register_company'),
    path('register/advisor/', AdvisorRegistrationView.as_view(), name='register_advisor'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('alive/', CompanyRegistrationView.as_view(), name='alive'),
]
