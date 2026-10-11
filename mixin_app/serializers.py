from rest_framework import serializers
from .models import *

class employeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = employeeModel
        fields = '__all__' 