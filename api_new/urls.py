from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api_new.views import GetMotocycle, StoreView, AeroView
from rest_framework import routers

router = DefaultRouter()
router.register(r'store', StoreView, basename="store")
router.register(r'aero', AeroView, basename="store")

urlpatterns = [
    path('moto/', GetMotocycle.as_view()),
    path('', include(router.urls))

]
