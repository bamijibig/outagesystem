"""
URL configuration for outagesystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from outage.views import GISSDSSView,GISFeederView,GISHightensionView,GISPowerTransmissionView,PowerTransmissionView, TechEngineerApprovalView, TechManagerApprovalView, TechSupervisorUpdateView

router=routers.DefaultRouter()
router.register('dss', GISSDSSView)
router.register('hightension', GISHightensionView)
router.register('feeder', GISFeederView)
router.register('pt', GISPowerTransmissionView)
router.register('powertrans', PowerTransmissionView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/',include(router.urls)),
    path('gisfeederstechmanager/<int:asset_id>/update/', TechManagerApprovalView.as_view(), name='update-gis-feeder'),
    path('gisfeederstechengineer/<int:asset_id>/update/', TechEngineerApprovalView.as_view(), name='update-giss-feeder'),
    path('gisfeedertechsupervisor/<int:asset_id>/update/', TechSupervisorUpdateView.as_view(), name='update-supervisor')
]
