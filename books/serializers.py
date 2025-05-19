from rest_framework import serializers
from .models import Book, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)  # Read-only nested category

    class Meta:
        model = Book
        fields = "__all__"
