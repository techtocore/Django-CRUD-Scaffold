from rest_framework import viewsets
from . import models
from . import serializers

class SampleObjectViewset(viewsets.ModelViewSet):
    queryset = models.SampleObject.objects.all()
    serializer_class = serializers.SampleObjectSerializer