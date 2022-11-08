from rest_framework import serializers

from api1.models import Category, Service, Houses, Cities


class CategorySerializer(serializers.Serializer):
    title = serializers.CharField()
    slug = serializers.SlugField()


class ServiceSerializerForSalon(serializers.Serializer):
    title = serializers.CharField()
    slug = serializers.SlugField()
    price = serializers.DecimalField(max_digits=5, decimal_places=2)
    category = CategorySerializer()


class SalonSerializer(serializers.Serializer):
    title = serializers.CharField()
    slug = serializers.SlugField()
    # service_set = ServiceSerializerForSalon(many=True)


class ServiceSerializer(serializers.Serializer):
    title = serializers.CharField()
    slug = serializers.SlugField()
    price = serializers.DecimalField(max_digits=5, decimal_places=2)
    salons = SalonSerializer(many=True)
    category = CategorySerializer()


class HousesSerializers(serializers.Serializer):
    adres = serializers.CharField()

    def update(self, instance, validated_data):
        instance.adres = validated_data.get('adres')
        instance.save()
        return instance

class CitiesSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=55)
    adres = HousesSerializers()


class PersonSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    rete = serializers.DecimalField(max_digits=8, decimal_places=2)
    house = serializers.SlugRelatedField(slug_field="adres", queryset=Houses.objects)


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.age = validated_data.get('age')
        instance.rete = validated_data.get('rete')
        instance.house = validated_data.get('house')
        instance.save()

        return instance

    # def save(self):
    #     title = self.validated_data['title']
    #     slug = self.validated_data['slug']
    #     price = self.validated_data['price']
    #     salons = self.validated_data['salons']
    #     category = self.validated_data['category']

# class ServiceMadelSerialisers(serializers.ModelSerializer):
#     class Meta:
#         model = Service
#         fields = "__all__"


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         exclude = ('id', 'slug')
#
#
# class ServiceSerializer(serializers.ModelSerializer):
#     category = CategorySerializer()
#     class Meta:
#         model = Service
#         fields = ('title', 'slug', 'price', 'category')
