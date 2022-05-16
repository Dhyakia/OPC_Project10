from django.conf import settings
from django.db import models


class Projects(models.Model):

    WEBSITE = 'WEB'
    ANDROID = 'ADR'
    IOS = 'IOS'

    TYPE_CHOICES = (
        (WEBSITE, "Website"),
        (ANDROID, "Android"),
        (IOS, "IOS"),
    )

    title = models.CharField(max_length=30)
    description = models.CharField(max_length=3000)
    type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
