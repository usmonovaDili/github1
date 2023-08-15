from datetime import datetime

from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import Books
from .serializers import BooksSerializers


class ListCreateViews(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializers


class UpdateDeleteViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializers


class GetByDateApiView(ListCreateViews):
    def get(self, request):
        status = request.query_params.get('status', True)
        day = request.query_params.get('day', '2023-08-10')
        print(status, day)
        data = datetime.strptime(day, '%Y-%m-%d').date()
        todos = Books.objects.filter(created_at__date=data, status=status)
        serializer = BooksSerializers(todos, many=True)
        return Response(serializer.data)
