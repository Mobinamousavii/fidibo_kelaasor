from django.urls import path
from base.views import purchasing

urlpatterns = [
    path('<int:book_id>/', purchasing), 
]
