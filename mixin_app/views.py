from django.shortcuts import render

from mixin_app.serializers import employeeSerializers
from .models import *
from rest_framework import mixins, generics

# Create your views here.
class employee(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = employeeModel.objects.all()
    serializer_class = employeeSerializers

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class employeeDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = employeeModel.objects.all()
    serializer_class = employeeSerializers

    def get(self, request, pk):
        return self.retrieve(request,pk)

    def put(self, request, pk):
        return self.update(request,pk)

    def delete(self, request, pk):
        return self.destroy(request,pk)