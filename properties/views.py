from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate

# User registration with role assignment
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        role = request.data.get('role')  # Role (buyer, seller, agent)

        # Create user
        user = User.objects.create_user(username=username, email=email, password=password)

        # Assign the user to the appropriate role group
        try:
            role_group = Group.objects.get(name=role)  # Fetch the role group (buyer, seller, or agent)
            user.groups.add(role_group)  # Add the user to the role group
        except Group.DoesNotExist:
            return Response({"message": "Role does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": f"User {role} created successfully"}, status=status.HTTP_201_CREATED)

# User login
@api_view(['POST'])
def login(request):
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
