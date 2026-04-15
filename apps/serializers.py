from rest_framework import serializers
from .models import Treking, Country, Camping, Caravan

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class TrekingSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Treking
        fields = '__all__'

class CampingSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Camping
        fields = '__all__'

class CaravanSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Caravan
        fields = '__all__'

