from django.db import models

# Create your models here.


class Location(models.Model):

    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    company = models.ForeignKey('aplicatie2.Companies', on_delete=models.CASCADE, related_name='companie')

    def __str__(self):
        return f"{self.city} {self.country}"
