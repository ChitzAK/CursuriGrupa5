from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from aplicatie2.models import Companies


class UserExtend(User):

    company = models.ForeignKey(Companies, on_delete=models.CASCADE)