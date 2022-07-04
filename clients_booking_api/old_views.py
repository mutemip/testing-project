from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from clients_booking_api.serializers.serializer import UserBookServiceSerializer
from booking_manager_api.models import EntityService, EntityBookingSchedule


class ClientBookingCreateView(APIView):
    """Entinty booking view"""

    serializer_class = UserBookServiceSerializer

    def post(request):
        entity_service_id = request.data.get("entity_service_id")
        booked_entity_schedule_id = request.data.get("entity_service_id")
        
        serializer = UserBookServiceSerializer(data=request.data)

        try:
            entity_service = EntityService.objects.get(pk=entity_service_id)

        except EntityService.DoesNotExist:
            return Response({"error": "Entity service not found"})

        try:
            booked_entity_schedule = EntityBookingSchedule.objects.get(
                pk=booked_entity_schedule_id
            )
        except EntityBookingSchedule.DoesNotExist:
            return Response({"error": "Entity booking schedule not found"})

        serializer.save(
            booked_by=request.user,
            booked_entity_service=entity_service,
            entity_booking_schedule=booked_entity_schedule
        )

        return Response({"status": "ok", "message": "Booking created successfully"})
