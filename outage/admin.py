from django.contrib import admin
from outage.models import GISDSS,GISHighTension,GISFeeders,PowerTransformers,GISTransmissionSubstations

admin.site.register(GISDSS)
admin.site.register(GISHighTension)
admin.site.register(GISFeeders)
admin.site.register(PowerTransformers)
admin.site.register(GISTransmissionSubstations)
