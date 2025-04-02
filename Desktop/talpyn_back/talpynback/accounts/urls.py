# accounts/urls.py
from django.urls import path
from .views import RegisterView, CurrentUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView, # Login - issues access and refresh tokens
    TokenRefreshView,    # Refreshes access token using refresh token
    # TokenVerifyView,   # Optional: verify token validity
)

# No app_name needed usually for APIs

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # LOGIN endpoint
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/verify/', TokenVerifyView.as_view(), name='token_verify'), # Optional
    path('user/', CurrentUserView.as_view(), name='current_user'), # Example protected endpoint
]