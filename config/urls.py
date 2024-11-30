from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from users.user.api.crud.login import CustomTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('config.utils.swagger')),
    path('api/students/', include('students.urls')),
    path('api/users/', include('users.user.urls')),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/organizations/', include('organizations.urls')),
    path('api/organization-degrees/', include('organizations.organization_degree.api.urls')),
    path('api/region/', include('students.region.api.urls')),
    path('api/shift/', include('students.shift.api.urls')),
    path('api/education_language/', include('education.education.api.urls')),

]
