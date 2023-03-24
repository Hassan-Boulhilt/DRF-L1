from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from jobs.models import JobOffer
from jobs.api.serializers import JobOfferSerializer


class JobOffer_List_Create_API_View(APIView):
    def get(self, request):
        job_offers = JobOffer.objects.filter(active=True)
        serializer = JobOfferSerializer(job_offers, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = JobOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)