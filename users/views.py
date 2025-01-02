from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from .serializers import UserSerializer, LoginSerializer
from django.contrib.auth import get_user_model
from rest_framework.decorators import action

User = get_user_model()

class AuthViewSet(ViewSet):
    """
    A ViewSet for handling user authentication and registration.
    """
    @action(detail=False, methods=['post'], url_path='register')
    def register(self, request):
        """
        Handles user registration with optional role assignment.
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # Save the user
            user = serializer.save()

            # Assign role if provided
            role = request.data.get('role')  # 'buyer', 'seller', or 'agent'
            if role:
                try:
                    role_group = Group.objects.get(name=role)
                    user.groups.add(role_group)
                except Group.DoesNotExist:
                    return Response({"message": "Role does not exist"}, status=status.HTTP_400_BAD_REQUEST)

            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='login')
    def login(self, request):
        """
        Handles user login and JWT token generation.
        """
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            # Authenticate user
            user = authenticate(username=username, password=password)
            if user:
                # Generate JWT tokens
                refresh = RefreshToken.for_user(user)
                return Response({
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "message": "Login successful"
                }, status=status.HTTP_200_OK)
            return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
