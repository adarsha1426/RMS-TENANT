from rest_framework import serializers
from users.models import CustomUser, UserProfile
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        token["password"] = user.password
        token["role"] = user.role
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data["id"] = self.user.id
        data["username"] = self.user.username
        data["role"] = self.user.role
        return data


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        if not username or not password:
            raise serializers.ValidationError("Invalid Username or Password")
        else:
            user = authenticate(
                username=attrs.get("username"), password=attrs.get("password")
            )
            if not user:
                raise serializers.ValidationError("Invalid Username or password")
            return attrs


class UserCreationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "first_name",
            "middle_name",
            "last_name",
            "password",
            "role",
        ]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = CustomUser(**validated_data)
        user.set_password(password)  # securely hashes the password
        user.save()
        return user


class UserProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "image": (instance.image.url if instance.image else ""),
            "address": instance.address or "",
            "date_of_birth": instance.date_of_birth or "",
            "gender": instance.gender or "",
        }


class UserProfileRetrieveUpdateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    email = serializers.EmailField(source="user.email")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    password = serializers.CharField(
        source="user.password", write_only=True, required=False
    )

    class Meta:
        model = UserProfile
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "image",
            "phone",
            "address",
            "date_of_birth",
            "gender",
        ]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user_data["password"] = make_password(user_data["password"])
        user = CustomUser.objects.create(**user_data)
        profile = UserProfile.objects.create(user=user, **validated_data)
        return profile

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", {})
        user = instance.user
        for attr, value in user_data.items():
            if attr == "password":
                setattr(user, attr, make_password("password"))
            else:
                setattr(user, attr, value)
        user.save()
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["first_name"] = instance.user.first_name.capitalize()
        rep["last_name"] = instance.user.last_name.capitalize()
        rep["middle_name"] = (
            instance.user.midlle_name if instance.user.middle_name else ""
        )
        rep["full_name"] = instance.get_full_name
        return rep
