# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Prefix your API endpoints (good practice)
    path('api/auth/', include('accounts.urls')),
    # You might have other API apps
    # path('api/posts/', include('posts.urls')),
]