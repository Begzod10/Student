"""
URL configuration for config project.

The `urlpatterns` list routes URLs to api. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function api
    1. Add an import:  from my_app import api
    2. Add a URL to urlpatterns:  path('', api.home, name='home')
Class-based api
    1. Add an import:  from other_app.api import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
    path('students/', include('students.urls')),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
