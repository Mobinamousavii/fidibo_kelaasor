from django.urls import path
from magazines.views import magazines, magazines_topic

urlpatterns = [
    path('', magazines),
    path('<str:topic>',magazines_topic),
]