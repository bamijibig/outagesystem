from django.shortcuts import render
from .models import GISDSS,GISFeeders,GISHighTension,GISTransmissionSubstations,PowerTransformers
from .serializers import GissdssSerializer,GisFeederSerializer,GisHighTensionSerializer,GisTransmissionSerializer,PowerTransformerSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class GISSDSSView(viewsets.ModelViewSet):
    queryset=GISDSS.objects.all()
    serializer_class=GissdssSerializer

class GISFeederView(viewsets.ModelViewSet):
    queryset=GISFeeders.objects.all()
    serializer_class=GisFeederSerializer

class GISHightensionView(viewsets.ModelViewSet):
    queryset=GISHighTension.objects.all()
    serializer_class=GisHighTensionSerializer

class GISPowerTransmissionView(viewsets.ModelViewSet):
    queryset=GISTransmissionSubstations.objects.all()
    serializer_class=GisTransmissionSerializer

class PowerTransmissionView(viewsets.ModelViewSet):
    queryset=PowerTransformers.objects.all()
    serializer_class=PowerTransformerSerializer

# views.py
class TechSupervisorUpdateView(APIView):
    def put(self,request,asset_id):
        try:
            gis_feeder=GISFeeders.objects.get(Assetid=asset_id)
            if not gis_feeder.Tech_supervisor:
                gis_feeder.Tech_supervisor=request.data.get('Tech_supervisor')
                gis_feeder.Tech_supervisor_comment=request.data.get('Tech_supervisor_comment')
                gis_feeder.Tech_supervisor_faultrectified=request.data.get('Tech_supervisor_faultrectified')
                gis_feeder.save()
                serializer=GisFeederSerializer(gis_feeder)
                return Response(serializer.data)
            else:
                return Response({"message": "Techsupervisor has already approved"}, status=status.HTTP_400_BAD_REQUEST)
        except GISFeeders.DoesNotExist:
            return Response({"message": "The Feeder does not exist"})
        
class TechEngineerApprovalView(APIView):
    def put(self,request,asset_id):
        try:
            gis_feeder=GISFeeders.objects.get(Assetid=asset_id)
            if gis_feeder.Tech_supervisor and not gis_feeder.Tech_engineer:
                 if gis_feeder.Tech_supervisor_faultrectified:
                    return Response({"message":"This has been fixed by technical supervisor"}, status=status.HTTP_400_BAD_REQUEST)
                 else:
                    gis_feeder.Tech_engineer=request.data.get('Tech_engineer')
                    gis_feeder.Tech_engineer_comment=request.data.get('Tech_engineer_comment')
                    gis_feeder.Tech_engineer_faultrectified=request.data.get('Tech_engineer_faultrectified')
                    gis_feeder.save()
                    serializer=GisFeederSerializer(gis_feeder)
                    return Response(serializer.data)
            else:
                return Response({"message": "Techengineer has already approved before"}, status=status.HTTP_400_BAD_REQUEST)
        except GISFeeders.DoesNotExist:
            return Response({"message": "Feeder does not exist"}, status=status.HTTP_404_NOT_FOUND)

class TechManagerApprovalView(APIView):
    def put(self, request, asset_id):
        try:
            gis_feeder = GISFeeders.objects.get(Assetid=asset_id)
            if  gis_feeder.Tech_engineer and not gis_feeder.Tech_manager:
                if gis_feeder.Tech_engineer_faultrectified:
                    return Response({"message": "This has already been approved by technical engineer"}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    gis_feeder.Tech_manager = request.data.get('Tech_manager')
                    gis_feeder.Tech_manager_comment=request.data.get('Tech_manager_comment')    
                    gis_feeder.Tech_manager_faultrectified= request.data.get('Tech_manager_faultrectified')
                    gis_feeder.save()
                    serializer = GisFeederSerializer(gis_feeder)
                    return Response(serializer.data)
            else:
                return Response({"message": "Tech_manager has already approved"}, status=status.HTTP_400_BAD_REQUEST)
        except GISFeeders.DoesNotExist:
            return Response({"message": "Asset not found"}, status=status.HTTP_404_NOT_FOUND)
        

        



