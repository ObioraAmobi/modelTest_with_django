from __future__ import unicode_literals
from django.db import models

class Contact(models.Model):

    class Meta: # include this to ensure build in IDE
        app_label = "modeltestapp"

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)

    # def __init__(self):
    #     pass

    def __str__(self):
        return ' '.join([
            self.first_name,
            self.last_name,
        ])