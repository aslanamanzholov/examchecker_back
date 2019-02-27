from django.urls import include, path

urlpatterns = [
    path('users/', include('examchecker_back.users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('exam/', include('examchecker_back.core.urls')),
]