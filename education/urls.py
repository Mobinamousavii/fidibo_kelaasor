from django.urls import path
from education.views import education, education_topic

urlpatterns = [
    path('', education),
    path('<str:topic>',education_topic),

]