from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Category, Service, Salon, Person, Houses, Cities
from .serializers import CategorySerializer, ServiceSerializer, SalonSerializer, PersonSerializer, HousesSerializers, \
    CitiesSerializers


#
# @api_view()
# def get_categoryes(request):
#     categoryes = Category.objects.all()
#     serializers = CategorySerializer(categoryes, many=True)
#     return Response(serializers.data)
#
#
# @api_view(['GET', 'POST'])
# def get_service(request):
#     service = Service.objects.all()
#     serializers = ServiceSerializer(service, many=True)
#     # if request.method == 'POST':
#     #     print('Do', request.data)
#     #     request.data['category'] = Category.objects.get(title=request.data['category']['title'])
#     #     print('Posle', request.data)
#     #     deser = ServiceSerializer(data=request.data)
#     #     if deser.is_valid():
#     #         deser.save()
#     return Response(serializers.data)
#
#
# # Рабочий вариант. но СЛАГ не уникален
# @api_view(['GET', 'POST'])
# def get_service(request):
#     services = Service.objects.all()
#     serializers = ServiceSerializer(services, many=True)
#     # if request.method == 'POST':
#     #     deser = ServiceSerializer(data=request.data)
#     #     serializer_category = CategorySerializer(data=request.data['category'])
#     #     if deser.is_valid(raise_exception=True) and serializer_category.is_valid(raise_exception=True):
#     #         print(deser)
#     #         s = Service()
#     #         s.title = deser.validated_data['title']
#     #         s.slug = deser.validated_data['slug']
#     #         s.price = deser.validated_data['price']
#     #         s.category = Category.objects.get(slug=request.data['category']['slug'])
#     #         print('category', s.category)
#     #         s.save()
#     return Response(serializers.data)
#
# @api_view()
# def get_service_for_title(request, text):
#     service = get_object_or_404(Service, title=text)
#     serializers = ServiceSerializer(service)
#     return Response(serializers.data)
#
#
# @api_view(['GET', 'POST'])
# def get_categoryes(request):
#     categoryes = Category.objects.all()
#     serializers = CategorySerializer(categoryes, many=True)
#     # if request.method == 'POST':
#     #     deser = CategorySerializer(data=request.data, many=True)
#     #     if deser.is_valid():
#     #         deser.save()
#     #         print("valid", deser)
#     #         # for i in deser.initial_data:
#     #         #     deser.save(**i)
#     #         # title = i['title']
#     #         # slug = i['slug']
#     #         # print("i", title, slug)
#     #         # category = Category.objects.create(title=title, slug=slug)
#
#     return Response(serializers.data)
#
#
# @api_view()
# def get_category_for_title(request, text):
#     categoryes = get_object_or_404(Category, title=text)
#     serializers = CategorySerializer(categoryes)
#     return Response(serializers.data)
#
#
# @api_view()
# def get_salon(request):
#     salon = Salon.objects.all()
#     serializers = SalonSerializer(salon, many=True)
#     return Response(serializers.data)

# class SalonView(ModelViewSet):
#     queryset = Salon.objects.all()
#     serializer_class = SalonSerializer
#
#
# class ServiceView(ModelViewSet):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer
#
#
# class CategoryView(ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


class ServicesAPiView(APIView):
    def get(self, request):
        queryset = Service.objects.all()
        serializers = ServiceSerializer(queryset, many=True)
        return Response(serializers.data)

    def post(self, request):
        data = ServiceSerializer(data=request.data)
        # print(request.data)
        if data.is_valid():
            print(data)
            s = Service()
            s.title = data.validated_data['title']
            s.slug = data.validated_data['slug']
            s.price = data.validated_data['price']
            s.category = Category.objects.get(**data.data['category'])
            s.save()
            s.salons.add(Salon.objects.get(pk=1))

            return Response({'1': 1})

        return Response({'status': 'hernay'})


@api_view(['GET', 'POST'])
def get_set_service(request):
    if request.method == 'POST':
        print(request.data)
        print(type(request.data))
    services = Service.objects.all()
    # serializers = ServiceSerializer(services, many=True)
    # return Response(serializers.data)


# @api_view(['GET', 'POST'])
# def get_person(request, pk=None):
#     if pk:
#         person = Person.objects.get(pk=pk)
#         serializer = PersonSerializer(person)
#         return Response(serializer.data)
#     persons = Person.objects.all()
#     serializer = PersonSerializer(persons, many=True)
#       if request.method == 'POST':
#           ser = PersonSerializer(data=request.data)
#           if ser.is_valid():
#               person_instance = Person.objects.get(pk=pk)
#               person_instance.name = ser.validated_data.get('name')
#               person_instance.save()
#               person_update = PersonSerializer(person_instance)
#               Response(person_update.data)

#     return Response(serializer.data)

"""обновление записи через функцию"""


@api_view(['GET', 'POST'])
def get_house(request, pk=None):
    house = Houses.objects.all()
    serializer = HousesSerializers(house, many=True)
    if request.method == 'POST':
        ser = HousesSerializers(data=request.data)
        print(ser.is_valid())
        if ser.is_valid():
            print(ser)
            ser.update(instance=get_object_or_404(Houses, pk=pk), validated_data=ser.validated_data)
        return Response(ser.data)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def get_person(request, pk=None):
    person = Person.objects.all()
    serializer = PersonSerializer(person, many=True)
    # if pk:
    #     person = Person.objects.get(pk=pk)
    #     serializer = PersonSerializer(person)
    #     return Response(serializer.data)
    if request.method == 'POST':
        ser = PersonSerializer(data=request.data)
        print(ser.is_valid())
        if ser.is_valid():
            ser.update(instance=get_object_or_404(Person, pk=pk), validated_data=ser.validated_data)
        return Response(ser.data)
    return Response(serializer.data)



@api_view()
def get_city(requsrst, pk=None):
    city = Cities.objects.all()
    serializers = CitiesSerializers(city, many=True)
    if requsrst.method == 'POST':
        data = CitiesSerializers(data=requsrst.data)
        if data.is_valid():
            data.update(instance=get_object_or_404(Cities, pk=pk), validated_data=data.validated_data)
            return Response(data.data)
    return Response(serializers.data)

"""Сделать апдейт при Форенкее и Манитумани"""
