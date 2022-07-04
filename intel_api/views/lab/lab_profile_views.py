from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import json


class LabList(APIView):
    """
    List all matching lab search results.
    """

    def post(self, request, format=None):
        lab_type = request.data.get("type")
        lab_data = request.data.get("lab_data")

        baseURL = "https://staging.panabios.org/api/external/search/lab/"

        payload = {
            "type": lab_type,
            "lab_data": lab_data
        }
        response = requests.post(baseURL, data=payload)
        json_data = json.loads(response.text)

        return Response(json_data, status=status.HTTP_200_OK)

    def get(self, request, format=None):

        # Code here

        return Response({}, status=status.HTTP_201_CREATED)


