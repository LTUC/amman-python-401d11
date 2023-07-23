
from rest_framework import serializers
from .models import Thing

class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thing
        fields =['id','owner', 'name', 'desc']
        # fields = '__all__'