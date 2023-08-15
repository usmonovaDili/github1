from rest_framework import serializers
from .models import Books, Author


class BooksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id', 'title', 'body', 'price', 'create_at', 'author']


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
