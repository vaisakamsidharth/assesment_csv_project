from django.urls import path 
from .views import CsvUploadView

urlpatterns = [
    path('api/upload/', CsvUploadView.as_view(), name='csv_upload'),
]