from jsonschema import ValidationError


from reservation.models import Table, Reservation

from rest_framework import serializers
from rest_framework.response import Response
from users.models import CustomUser


class TableListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"


class TableCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"


class TableRetireveUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"

    """
    TODO: 
        1.Refactor the code and use validate() for validating instead in update() and create() method.
        2.Use single serializer for ListCreateRetrieveUpdateDestroy
    """


class ReservationSerializer(serializers.Serializer):

    table = serializers.PrimaryKeyRelatedField(queryset=Table.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    phone = serializers.CharField(max_length=10)
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()
    grace_time = serializers.CharField(max_length=100, allow_blank=True)
    guests = serializers.IntegerField()

    def create(self, validated_data):
        return Reservation.objects.create(**validated_data)

    def update(self, instance: Reservation, validated_data):
        table = validated_data.pop("table")
        if instance.table.status == "new" or instance.table.status == "completed":
            instance.table.status == "pending"
            instance.table.save()

        return super().update(instance, validated_data)


class ReservationRetirieveUpdateDestroySerializer(serializers.Serializer):

    table = serializers.PrimaryKeyRelatedField(queryset=Table.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    phone = serializers.CharField(
        max_length=15,
    )
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()
    grace_time = serializers.CharField()
    guests = serializers.CharField()

    def validate(self, attrs):
        table = attrs["table"]
        start_time = attrs["start_time"]
        end_time = attrs["end_time"]
        phone = attrs["phone"]
        grace_time = attrs["grace_time"]

        if Reservation.objects.filter(
            table=table, start_time__lt=end_time, end_time__gt=start_time, phone=phone
        ).exists():
            raise ValidationError(f"Sorry! {table.name} has already been booked.")
        return attrs

    def create(self, validated_data):
        return Reservation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["table_status"] = instance.table.status
        data["first_name"] = (
            instance.user.first_name if instance.user.first_name else None
        )
        return data
