from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NewsViewSet, NewsViewOrganizationList, NewsBlockViewSet

router = DefaultRouter()
router.register(r'news', NewsViewSet, basename='news')
router.register(r'news_block', NewsBlockViewSet, basename='news_block')

urlpatterns = [
    path('', include(router.urls)),
    path('news_list/', NewsViewOrganizationList.as_view(), name='news-organization'),
]
