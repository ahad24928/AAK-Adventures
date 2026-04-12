from rest_framework import serializers
from .models import Treking, Country

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class TrekingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treking
        fields = '__all__'