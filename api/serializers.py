from rest_framework import serializers
from staff.models import ManagerInfo, EmpInfo


class EmpInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpInfo
        exclude = '__all__'

