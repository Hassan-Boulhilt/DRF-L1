from django.urls import path
from jobs.api.views import JobOffer_List_Create_API_View


urlpatterns = [
    path("job-offers/", JobOffer_List_Create_API_View.as_view(), name="job-offers"),
]