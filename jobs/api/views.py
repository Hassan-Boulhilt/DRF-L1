from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from jobs.models import JobOffer
from jobs.api.serializers import JobOfferSerializer


class JobOffer_List_Create_API_View(APIView):
    def get(self, request):
        job_offers = JobOffer.objects.filter(job_available=True)
        serializer = JobOfferSerializer(job_offers, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = JobOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class JobOffer_Detail_API_View(APIView):
    def get_object(self, pk):
        try:
            return JobOffer.objects.get(pk=pk)
        except JobOffer.DoesNotExist:
            return Response({"error": {"code": 404, "message": "Job Offer not found!"}}, status=status.HTTP_404_NOT_FOUND)
    def get(self, request, pk):
        job_offer = self.get_object(pk)
        serializer = JobOfferSerializer(job_offer)
        return Response(serializer.data)
    def put(self, request, pk):
        job_offer = self.get_object(pk)
        serializer = JobOfferSerializer(job_offer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        job_offer = self.get_object(pk)
        job_offer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)