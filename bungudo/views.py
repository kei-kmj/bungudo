from rest_framework import viewsets
from rest_framework.response import Response
from bungudo.serializers import HelloSerializer


class HelloView(viewsets.ViewSet):
    def list(self, request):
        serializer = HelloSerializer({'message': 'Hello, World!'})
        return Response(serializer.data)
