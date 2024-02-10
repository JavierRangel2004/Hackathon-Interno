# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AdvisorRegistrationView, CompanyRegistrationView,
    CompanyProfileUpdateView,
    AdvisorProfileUpdateView,
    CertificationViewSet,
    ForumPostViewSet,
    CompanyViewSet,
    AdvisorViewSet,
    CustomTokenObtainPairView
)
from rest_framework_simplejwt.views import TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'certifications', CertificationViewSet)
router.register(r'forumposts', ForumPostViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'advisors', AdvisorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/advisor/', AdvisorRegistrationView.as_view(), name='register_advisor'),
    path('register/company/', CompanyRegistrationView.as_view(), name='register_company'),
    path('profile/company/', CompanyProfileUpdateView.as_view(), name='company_profile_update'),
    path('profile/advisor/', AdvisorProfileUpdateView.as_view(), name='advisor_profile_update'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)