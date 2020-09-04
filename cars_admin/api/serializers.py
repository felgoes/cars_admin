from rest_framework import serializers

from ..models import Partner, Brand, VehicleModel, Vehicle


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class VehicleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['name', 'document_id', 'user', 'reg_id']


class OwnerSerializer(serializers.ModelSerializer):
    vehicles = serializers.StringRelatedField(many=True)

    class Meta:
        model = Partner
        fields = ['name', 'document_id', 'vehicles', 'reg_id']
