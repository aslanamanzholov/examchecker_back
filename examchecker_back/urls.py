from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    url(r'api/docs', include_docs_urls(title='My API title'))
]
