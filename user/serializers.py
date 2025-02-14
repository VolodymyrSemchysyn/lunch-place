from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from django.utils.translation import gettext as _

from user.models import Employee, Vote


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "email", "password", "is_staff")
        read_only_fields = ("is_staff",)
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update a user, set the password correctly and return it"""
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(label=_("Email"))
    password = serializers.CharField(
        label=_("Password"), style={"input_type": "password"}
    )

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user = authenticate(email=email, password=password)

            if user:
                if not user.is_active:
                    msg = _("User account is disabled.")
                    raise serializers.ValidationError(
                        msg, code="authorization"
                    )
            else:
                msg = _("Unable to log in with provided credentials.")
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = _("Must include 'username' and 'password'.")
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs


class EmployeeSerializer(serializers.ModelSerializer):
    """Serializer for Employee model."""

    user = UserSerializer()

    class Meta:
        model = Employee
        fields = ["id", "user", "name", "position", "date_of_birth"]

    def create(self, validated_data):
        """Create a new Employee with associated user."""
        user_data = validated_data.pop("user")
        user = get_user_model().objects.create_user(**user_data)
        employee = Employee.objects.create(user=user, **validated_data)
        return employee


class VoteSerializer(serializers.ModelSerializer):
    """Serializer for Vote model."""

    class Meta:
        model = Vote
        fields = ["id", "employee", "menu", "vote_value"]