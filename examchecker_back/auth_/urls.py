from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import refresh_jwt_token

from .views import AuthViewSet, UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, base_name='user')
urlpatterns = router.urls
urlpatterns += [url(r'^api-token-refresh/', refresh_jwt_token),]
