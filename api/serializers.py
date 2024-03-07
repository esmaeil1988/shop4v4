from rest_framework import serializers
from app1.models import product

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields=("title","price","moshakhasat","brand","tozih","garenty")