from django.db import models

class GISDSS(models.Model):
    Assetid = models.IntegerField(primary_key=True)
    StaffID = models.IntegerField()
    AssetType = models.CharField(max_length=255)
    
    def __str__(self):
        return str(self.Assetid)

class GISHighTension(models.Model):
    AssetType = models.CharField(max_length=255)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    NACCode = models.CharField(max_length=255)
    DSS11KV415VParent = models.ForeignKey(GISDSS, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.AssetType)

class GISFeeders(models.Model):
    Assetid = models.IntegerField(primary_key=True)
    AssetName = models.CharField(max_length=255)
    AssetType = models.CharField(max_length=255)
    FeederName = models.CharField(max_length=255)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    NACCode = models.CharField(max_length=255)
    HT11KVParent = models.ForeignKey(GISHighTension, on_delete=models.SET_NULL, null=True)
    Tech_manager=models.BooleanField(default=False)
    Tech_manager_comment=models.CharField(max_length=255, default='no comment')
    Tech_manager_faultrectified=models.BooleanField(default=False)
    Tech_engineer=models.BooleanField(default=False)
    Tech_engineer_comment=models.CharField(max_length=255, default='no comment')
    Tech_engineer_faultrectified=models.BooleanField(default=False)
    Tech_supervisor=models.BooleanField(default=False)
    Tech_supervisor_comment=models.CharField(max_length=255, default='no comment')
    Tech_supervisor_faultrectified=models.BooleanField(default=False)
    

    def __str__(self):
        return str(self.Assetid)


class PowerTransformers(models.Model):
    Assetid = models.IntegerField(primary_key=True)
    AssetType = models.CharField(max_length=255)
    PT33KV11KVName = models.CharField(max_length=255)
    PT33KV11KVParent = models.ForeignKey(GISFeeders, on_delete=models.SET_NULL, null=True)
    

    def __str__(self):
        return str(self.Assetid)


class GISTransmissionSubstations(models.Model):
    Assetid = models.IntegerField(primary_key=True)
    AssetName = models.CharField(max_length=255)
    AssetType = models.CharField(max_length=255)
    CaptureDateTime = models.DateTimeField()
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    NACCode = models.CharField(max_length=255)
    TS132KVName = models.CharField(max_length=255)
    TS132KVRating = models.CharField(max_length=255)
    TSAIN = models.CharField(max_length=255)
    Powertrans = models.ForeignKey(PowerTransformers, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return str(self.Assetid)

