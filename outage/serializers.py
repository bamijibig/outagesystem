from .models import GISTransmissionSubstations,GISDSS,GISFeeders,GISHighTension,PowerTransformers
from rest_framework import serializers

class GissdssSerializer(serializers.ModelSerializer):
    class Meta:
        model=GISDSS
        fields="__all__"


class GisHighTensionSerializer(serializers.ModelSerializer):
    dss=GissdssSerializer(read_only=True)
    class Meta:  
        model=GISHighTension
        fields="__all__"
        # ['dss','id','AssetType','Latitude','Longitude','NACCode','DSS11KV415VParent']
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['dss'] = GissdssSerializer(instance.DSS11KV415VParent).data
        return representation
        

class GisFeederSerializer(serializers.ModelSerializer):
    hightension=GisHighTensionSerializer(read_only=True)
    class Meta:
        model=GISFeeders
        fields="__all__"
        # ['hightension','Assetid','AssetName','AssetType','FeederName','Latitude','Longitude','NACCode','HT11KVParent']
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['hightension'] = GisHighTensionSerializer(instance.HT11KVParent).data
        return representation    

class PowerTransformerSerializer(serializers.ModelSerializer):
    #feeder=GisFeederSerializer(read_only=True)
    class Meta:
        model=PowerTransformers
        fields="__all__"
        # fields=['feeder','Assetid','AssetType','PT33KV11KVName','PT33KV11KVParent']
    def to_representation(self, instance):
        representation = super().to_representation(instance) 
        representation['feeder'] = GisFeederSerializer(instance.PT33KV11KVParent).data
        return representation  

class GisTransmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model=GISTransmissionSubstations
        fields="__all__"  
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['powertrans'] = PowerTransformerSerializer(instance.Powertrans).data
        return representation


##########################################################################################



