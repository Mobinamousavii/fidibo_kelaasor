from django.urls import path
from audiobooks.views import audiobooks, audiobook_topic

urlpatterns = [
    path('', audiobooks),
    path('<str:topic>',audiobook_topic),

]
