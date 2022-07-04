import grpc
from django_grpc_framework.services import Service
from clients_booking_api.models import UserBookService
from .serializers import UserBookServiceProtoSerializer
import logging


class UserBookServiceServices(Service):

    def GetBookedServiceByCode(self, request, context):
        code = request.code
        userbookservice = UserBookService.get_user_book_service_by_code(code=code)
        serializer = UserBookServiceProtoSerializer(userbookservice)
        return serializer.message
