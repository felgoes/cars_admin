from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from ..models import Partner, Brand, VehicleModel, Vehicle
from django.contrib.auth.models import User

from .serializers import PartnerSerializer, \
    BrandSerializer, \
    VehicleModelSerializer, \
    VehicleSerializer


# PROPRIETÁRIO
class OwnerViewSet(ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class OwnerDocViewSet(ModelViewSet):
    serializer_class = PartnerSerializer
    lookup_field = 'doc'

    def get_queryset(self):
        return Partner.objects.filter(document_id=self.kwargs['doc'])


class OwnerMatViewSet(ModelViewSet):
    serializer_class = PartnerSerializer
    lookup_field = 'mat'

    def get_queryset(self):
        return Partner.objects.filter(reg_id=self.kwargs['mat'])


class OwnerCreateViewSet(ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

    def create(self, request, *args, **kwargs):
        user = User.objects.filter(username=request.user).first()
        request.data.update({'user': user.id})
        super(OwnerCreateViewSet, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created",
                    "result": request.data}
        return Response(response)


# VEÍCULOS
class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class VehicleModelViewSet(ModelViewSet):
    queryset = VehicleModel.objects.all()
    serializer_class = VehicleModelSerializer


class VehicleListViewSet(ModelViewSet):
    serializer_class = VehicleSerializer

    def get_queryset(self):
        user = self.request.user
        vehicle = Vehicle.objects.filter(user=user.id)
        if vehicle:
            return vehicle
        else:
            return Response({'erro: Nenhum veículo encontrado para este usuário'})


class VehiclePlateListViewSet(ModelViewSet):
    serializer_class = VehicleSerializer
    lookup_field = 'placa'

    def get_queryset(self):
        user = self.request.user
        person = Partner.objects.filter(user=user).first()
        if person:
            vehicle = Vehicle.objects.filter(plate_num=self.kwargs['placa'], user=user)
            if vehicle:
                return vehicle


class VehicleChassisListViewSet(ModelViewSet):
    serializer_class = VehicleSerializer
    lookup_field = 'chass'

    def get_queryset(self):
        user = self.request.user
        person = Partner.objects.filter(user=user).first()
        if person:
            vehicle = Vehicle.objects.filter(chassis_num=self.kwargs['chass'], user=user)
            if vehicle:
                return vehicle


class VehicleDocListViewSet(ModelViewSet):
    serializer_class = VehicleSerializer
    lookup_field = 'doc'

    def get_queryset(self):
        user = self.request.user
        person = Partner.objects.filter(user=user).first()
        if person:
            vehicle = Vehicle.objects.filter(owner__document_id=self.kwargs['doc'], user=user)
            if vehicle:
                return vehicle


class VehicleCreateViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def create(self, request, *args, **kwargs):
        brand = Brand.objects.filter(slug=request.data.get('brand')).first()
        model = VehicleModel.objects.filter(slug=request.data.get('model')).first()
        owner = Partner.objects.filter(name=request.data.get('owner')).first()
        user = User.objects.filter(username=request.user).first()
        request.data.update({'user': user.id})
        request.data.update({'type': car_type.id})
        request.data.update({'brand': brand.id})
        request.data.update({'model': model.id})
        request.data.update({'owner': owner.id})

        super(VehicleCreateViewSet, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created",
                    "result": request.data}
        return Response(response)
