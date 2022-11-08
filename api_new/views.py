from django.db.models import Q, F
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from api_new.models import Moto, Store, Aero
from api_new.serializers import MotoSerializers, StoreSerializers, AeroSerializer


# Create your views here.
class GetMotocycle(APIView):

    def get(self, request):
        queryset = Moto.objects.all()
        serializer = MotoSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = MotoSerializers(data=request.data)
        if data.is_valid():
            print(data)
            moto = Moto()
            moto.brand = data.validated_data['brand']
            moto.model = data.validated_data['model']
            moto.price = data.validated_data['price']
            moto.save()
            print(moto)
        else:
            print('chto ni kak')

        return Response({'all': 'ok'})


# def get_Q_and_F(request):
#     queryset = Moto.objects.filter(Q(concern__title="ИЖ Со") | Q(concern__title='Minsk Со'))
#     print(queryset)
#     print(queryset.update(price=F('price')*2))
#
#     for i in queryset:
#         print(i.__dict__)
#     return Response({"1": 1})


class StoreView(viewsets.ViewSet):
    def list(self, request):
        queryset = Store.objects.all()
        serializers = StoreSerializers(queryset, many=True)

        return Response(serializers.data)

    def retrieve(self, request, pk=None):
        queryset = Store.objects.all()
        store = get_object_or_404(queryset, pk=pk)
        serializers = StoreSerializers(store)

        return Response(serializers.data)

    def destroy(self, request, pk=None):
        store = Store.objects.get(pk=pk)
        store.delete()

        return Response({'1': 'delete'})


class AeroView(viewsets.ViewSet):
    def list(self, request):
        queryset = Aero.objects.all()
        serializer = AeroSerializer(queryset, many=True)

        return Response(serializer.data)

    def update(self, request, pk=None):
        aero = Aero.objects.get(pk=pk)
        deserializer = AeroSerializer(instance=aero, data=request.data)
        if deserializer.is_valid():
            print("True")
            deserializer.save()

        return Response(deserializer.data)
