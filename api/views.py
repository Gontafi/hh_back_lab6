from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from . import models, serializers


class CompanyList(generics.ListCreateAPIView):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer


class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer


class VacancyList(generics.ListCreateAPIView):
    queryset = models.Vacancy.objects.all()
    serializer_class = serializers.VacancySerializer


class VacancyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Vacancy.objects.all()
    serializer_class = serializers.VacancySerializer


class VacancyByCompanyList(generics.ListAPIView):
    serializer_class = serializers.VacancySerializer

    def get_queryset(self):
        company_id = self.kwargs['id']
        return models.Vacancy.objects.filter(company__id=company_id)


class TopTenVacancies(generics.ListAPIView):
    queryset = models.Vacancy.objects.order_by('-salary')[:10]
    serializer_class = serializers.VacancySerializer


class VacancySubmit(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, id):

        vacancy = get_object_or_404(models.Vacancy, pk=id)
        serializer = serializers.VacancySerializer(vacancy)

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'vacancy_submit',
            {
                'type': 'submit.vacancy',
                'message': serializer.data
            },
        )

        return Response(serializer.data, status=status.HTTP_200_OK)

