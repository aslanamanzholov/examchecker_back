from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path
from rest_framework.permissions import AllowAny
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('examchecker_back.users.urls')),
    path('exam/', include('examchecker_back.core.question.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'api/docs', include_docs_urls(title='My API title', permission_classes=[AllowAny]))
]
