from unicodedata import category
from .models import Products
from rest_framework import serializers


class POLLSerializer(serializers.ModelSerializer):
    # categories = serializers.StringRelatedField(many=False)
    # sub_categories = serializers.StringRelatedField(many=False)
    # color = serializers.StringRelatedField(many=False)
    # size = serializers.StringRelatedField(many=False)
    class Meta:
        model = Products
        fields = "__all__"