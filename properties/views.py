from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework import status
from .models import Property
from .serializers import PropertySerializer

class AuthViewSet(ViewSet):
    """
    A ViewSet for user authentication and registration.
    """

    def register(self, request):
        """
        Handles user registration with role assignment.
        """
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        role = request.data.get('role')  # Role (buyer, seller, agent)

        # Validate input
        if not username or not email or not password or not role:
            return Response({"message": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"message": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            return Response({"message": "Email already registered"}, status=status.HTTP_400_BAD_REQUEST)

        # Create user
        user = User.objects.create_user(username=username, email=email, password=password)

        # Assign the user to the appropriate role group
        try:
            role_group = Group.objects.get(name=role)  # Fetch the role group (buyer, seller, or agent)
            user.groups.add(role_group)  # Add the user to the role group
        except Group.DoesNotExist:
            return Response({"message": "Role does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": f"User {role} created successfully"}, status=status.HTTP_201_CREATED)

    def login(self, request):
        """
        Handles user login and JWT token generation.
        """
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

class PropertyViewSet(ModelViewSet):
    """
    A ViewSet for listing, creating, and managing properties.
    """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer