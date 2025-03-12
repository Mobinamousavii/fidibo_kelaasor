from django.urls import path
from ebooks.views import ebooks, ebook_topic

urlpatterns = [
    path('',ebooks),
    path('<str:topic>', ebook_topic)
]
