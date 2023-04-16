from rest_framework import serializers
from . import models


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Company
        fields = '__all__'


class VacancySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Vacancy
        fields = '__all__'