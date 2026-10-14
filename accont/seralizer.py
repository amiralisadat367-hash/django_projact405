from rest_framework import serializers
from .models import Accont

class AccontSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accont
        fileds = "__all__"