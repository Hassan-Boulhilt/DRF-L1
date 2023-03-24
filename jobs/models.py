from django.db import models

class JobOffer(models.Model):
    job_company = models.CharField(max_length=120)
    job_email = models.EmailField()
    job_title = models.CharField(max_length=120)
    job_description = models.TextField()
    job_location = models.CharField(max_length=120)
    job_salary = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    job_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.job_title} {self.job_location}"
