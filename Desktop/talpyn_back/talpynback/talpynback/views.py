# accounts/views.py
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer, RegisterSerializer

User = get_user_model()

# 1. Registration View
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,) # Anyone can register
    serializer_class = RegisterSerializer
    # No need to log in user here, frontend will request token separately

# 2. Login View (using SimpleJWT's default view)
# SimpleJWT provides views to obtain and refresh tokens.
# We just need to point a URL to them. (See urls.py below)
# You can customize the serializer if needed:
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#         # Add custom claims
#         token['username'] = user.username
#         # ...
#         return token
# class MyTokenObtainPairView(TokenObtainPairView):
#      serializer_class = MyTokenObtainPairSerializer


# 3. Example Protected View (Get Current User)
class CurrentUserView(APIView):
    permission_classes = [permissions.IsAuthenticated] # Only authenticated users

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

# Note: SimpleJWT handles logout by the client simply discarding the token.
# For added security, you can implement token blacklisting if needed.