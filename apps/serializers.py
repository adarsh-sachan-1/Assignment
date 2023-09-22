"""
serializer file
"""
# django import
from rest_framework import serializers
# local import
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    """
    write a serializer for Article
    """
    class Meta:
        """Article models used"""
        model = Article
        fields = '__all__'
