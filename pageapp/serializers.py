from rest_framework import serializers
from .models import Category,Sumka


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class Sumkaserializers(serializers.ModelSerializer):
    category = CategorySerializers(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )
    class Meta:
        model = Sumka
        fields = ['id', 'firmasi', 'rangi', 'materiali', 'davlati', 'category', 'category_id']