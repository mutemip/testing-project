from rest_framework import generics, status
from rest_framework.response import Response
from intel_api.views.authentication import GetRequestAuthenticationBase
from rest_framework.views import APIView

from clients_booking_api.models import UserBookService
from clients_booking_api.serializers import ManagerUserBookServiceSerializer


class ExternalEntityBookingView(GetRequestAuthenticationBase,APIView):

    serializer_class = ManagerUserBookServiceSerializer

    def get(self,request):
        try:
            user = self.authenticate(request)
        except Exception as e:
            return Response({"status":"error","message":"%s"%str(e)},status=status.HTTP_401_UNAUTHORIZED) 

        try:
            external_entity = user.get_external_entity()
            if external_entity:
                booked_services = UserBookService.get_external_entity_bookings(external_entity)
                return Response({"status":"success","data":self.serializer_class(booked_services,many=True).data},status=status.HTTP_200_OK)
            else:
                return Response({"status":"error","message":"Unauthorized user access."},status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({"status":"error","message":"Error occured(%s)"%str(e)},status=status.HTTP_400_BAD_REQUEST)


            