from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import JsonResponse

class templateAPIView(APIView):
    def get(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        data = {'key': self.request.session.session_key}
        return JsonResponse(data, status=status.HTTP_200_OK)