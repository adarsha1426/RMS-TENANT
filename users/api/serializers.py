from rest_framework import serializers
from users.models import CustomUser, UserProfile
from django.contrib.auth.hashers import make_password


class UserCreationSerializer(serializers.ModelSerializer):
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

    extra_kwargs = {"password": {"write_only": True}}


class UserProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


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
        rep["middle_name"] = instance.user.midlle_name if instance.user.middle else ""
        return rep
