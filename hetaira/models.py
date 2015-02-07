from django.db import models

class ReportedEntity(models.Model):
    identifier = models.CharField(max_length=128,primary_key=True)
    vi = models.IntegerField()
    np = models.IntegerField()
    hg = models.IntegerField()
    ns = models.IntegerField()
    nc = models.IntegerField()
    dr = models.IntegerField()
    po = models.IntegerField()
    st = models.IntegerField()
    ph = models.IntegerField()

class InitialSettings(models.Model):
    salt = models.CharField(max_length=128)
    twilio_sid = models.CharField(max_length=128)
    twilio_authtoken = models.CharField(max_length=128)
