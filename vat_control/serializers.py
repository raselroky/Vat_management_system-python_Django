from rest_framework import serializers
from .models import VAT

class VATSerializers(serializers.ModelSerializer):
    class Meta:
        model=VAT
        fields=('__all__')