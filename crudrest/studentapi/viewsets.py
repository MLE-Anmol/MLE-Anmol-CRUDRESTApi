from rest_framework import viewsets
from . import models
from . import serializers

class StudentViewset(viewsets.ModelViewSet):
    queryset = model.Student.objects.all()
    serializer_class = serializers.StudentSerializer