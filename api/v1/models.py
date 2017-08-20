from django.db import models

#creating the model class Contacts
class Contacts(models.Model):
    name = models.CharField(max_length=500)
    msisdn = models.CharField(max_length=11)
    address = models.TextField()

    def __str__(self):
        return self.name

    def get_msisdn(self):
        return self.msisdn

    def get_address(self):
        return self.address