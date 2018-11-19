from rest_framework import serializers
from . import models

class SampleObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SampleObject
        fields = ('key', 'value')