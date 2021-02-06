from django.urls import path
from .views import templateAPIView

urlpatterns = [
    path('template', templateAPIView.as_view()),
]