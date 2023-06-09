from rest_framework import serializers
from app.models import *
class Myshow(serializers.ModelSerializer):
    class Meta:
        model=BookMyShow
        fields='__all__'