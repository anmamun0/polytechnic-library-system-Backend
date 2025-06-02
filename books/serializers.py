from rest_framework import serializers
from .models import Book, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)  # Read-only nested category
    viewers_profile = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = "__all__"
    def get_viewers_profile(self,obj):
        transactions = obj.book_transactions.all()
        profile_ids = list({tx.profile.id for tx in transactions if tx.profile})
        return profile_ids