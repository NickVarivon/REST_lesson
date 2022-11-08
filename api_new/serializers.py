from rest_framework import serializers


class ConcernSerialisers(serializers.Serializer):
    title = serializers.CharField()
    city = serializers.CharField()


class StoreSerializers(serializers.Serializer):
    title = serializers.CharField()
    concern = ConcernSerialisers()


class MotoSerializers(serializers.Serializer):
    brand = serializers.CharField()
    model = serializers.CharField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    concern = ConcernSerialisers(many=True)


class AeroSerializer(serializers.Serializer):
    city = serializers.CharField()
    title = serializers.CharField()

    def update(self, instance, validated_data):
        instance.city = validated_data.get('city', instance.city)
        instance.title = validated_data.get('title', instance.title)
        return instance



class AviaSerializer(serializers.Serializer):
    brand = serializers.CharField()
    model = serializers.CharField()
    price = serializers.IntegerField()
    aeroport = AeroSerializer(many=True)
