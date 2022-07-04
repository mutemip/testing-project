from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests


class CertificateList(APIView):
    """
    List all matching certificates search results.
    """

    def get(self, request, format=None):
        keyword = request.data.get("search_keywork")
        response = requests.get("url", keyword)
        data = response.text
        return Response({data}, status=status.HTTP_201_CREATED)

    def post(self, request, format=None):

        return Response({}, status=status.HTTP_201_CREATED)