from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

from restaurant.mixins import VersionedAPIView
from user.models import Employee, Vote
from user.serializers import UserSerializer, EmployeeSerializer, VoteSerializer


class CreateUserView(VersionedAPIView, generics.CreateAPIView):
    """View to create a new user."""
    serializer_class = UserSerializer


class ManageUserView(VersionedAPIView, generics.RetrieveUpdateAPIView):
    """View to manage authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class CreateEmployeeView(VersionedAPIView, generics.CreateAPIView):
    """View to create a new Employee."""
    serializer_class = EmployeeSerializer


class EmployeeListView(VersionedAPIView, generics.ListAPIView):
    """View to list all Employees. Accessible only by admin."""
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.select_related("user")
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAdminUser,)


class EmployeeDetailView(VersionedAPIView, generics.RetrieveUpdateAPIView):
    """View to manage an authenticated employee's profile."""
    serializer_class = EmployeeSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        """Return the employee object of the currently authenticated user."""
        return self.request.user.employee


class CreateVoteView(VersionedAPIView, generics.CreateAPIView):
    """View to create a new Vote."""
    serializer_class = VoteSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)


class VoteListView(VersionedAPIView, generics.ListAPIView):
    """View to list all Votes."""
    serializer_class = VoteSerializer
    queryset = Vote.objects.select_related("employee", "menu")
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)