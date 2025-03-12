from django.urls import path
from fidiplus.views import fidiplus

urlpatterns = [
    path('', fidiplus),
]