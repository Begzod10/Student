from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from users.user.api.crud.login import CustomTokenObtainPairView, CustomTokenRefreshView

urlpatterns = [
    path('get/admin/', admin.site.urls),
    path('get/', include('config.utils.swagger')),
    path('get/students/', include('students.urls')),
    path('get/users/', include('users.user.urls')),
    path('get/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('get/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('get/organizations/', include('organizations.urls')),
    path('get/organization-degrees/', include('organizations.organization_degree.api.urls')),
    path('get/region/', include('students.region.api.urls')),
    path('get/shift/', include('students.shift.api.urls')),
    path('get/education_language/', include('education.education.api.urls')),
    path('get/organization_fields/', include('organizations.organization_fields.urls')),
    path('get/test/', include('test.urls'))

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
