
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema')),
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema')),
    path('admin/', admin.site.urls),
    path('api/v1/', include('books.urls')),
    path('api/v1/', include('loans.urls')),
    path('api/v1/', include('users.urls')),
    path('api/v1/', include('history.urls')),
]
