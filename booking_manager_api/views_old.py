# from django.shortcuts import get_object_or_404
# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
#
# from datetime import date, timedelta
#
# from .models import AvailableLabs , DateAndSlot , Lab
# from clients_booking_api.models import LabBooking
#
#
# class CreateSlotView(APIView):
#     """View for adding slot using DateSlot Model."""
#     def post(request):
#         pass
#
#
# class SlotListView(APIView):
#     def get(request):
#         slot_list_booked = DateAndSlot.objects.filter(labs_added = True).order_by('booking_date') # query for slot for which labs are alloted
#         slot_list_unbooked = DateAndSlot.objects.filter(labs_added = False).order_by('booking_date') # query for slot for which labs are not alloted
#
#         content = {
#             'slot_list_booked': slot_list_booked ,
#             'slot_list_unbooked' : slot_list_unbooked
#         }
#         return Response(content)
#
# class BookingsCreateView(APIView):
#     """Creating available lab reservation per date for a particular slot"""
#
#     def post(request , slot_id = None):
#         serializer = ''
#         selected_slot_obj = DateAndSlot.objects.get(pk = slot_id) # get slot for a particular id .
#
#         if request.POST:
#             # generate lab objects for a particular slot
#             n = AvailableLabs(booking_date_slot = selected_slot_obj )
#             # serializer(request.POST , instance = n)
#
#             if serializer.is_valid():
#                 serializer.save()
#                 n.save()
#
#                 for lab_no in range(1 ,n.labs_available+1):
#                     r = Lab(chosen_date_slot = selected_slot_obj , lab = lab_no )
#                     r.save()
#
#                 ds = DateAndSlot.objects.get(pk = slot_id)
#                 ds.labs_added = True
#                 ds.save()
#                 return Response({"message":"Booking resaver"})
#
#         return Response({"error":serializer.error})
#
#
# class AllBookedDatesListView(APIView):
#     """Get all the slot dates for which user has done bookings"""
#     def get(request):
#         booking_dates = DateAndSlot.objects.filter(labs_added=True).order_by('booking_date')
#         content = {
#             'booking_dates' : booking_dates
#         }
#         return Response(content)
#
# class SlotBookingDetailView(APIView):
#     """Get all the bookings for selected slot"""
#     def get(request, slot_id):
#         bookings_per_date = LabBooking.objects.filter(booking_date_slot = slot_id).order_by('booked_lab')
#         content = {
#                 'bookings_per_date' : bookings_per_date
#         }
#         return Response(content)
#
#
# class UserBookingDetailView(APIView):
#     """Get details of User Booking"""
#     def get(request , booking_id):
#         user_booking_detail = get_object_or_404(LabBooking , pk = booking_id)
#         content = {
#             'user_booking' : user_booking_detail
#         }
#         return Response(content)
#
#     def delete(request , booking_id):
#         user_booking_detail = get_object_or_404(LabBooking , pk = booking_id)
#         user_booking_detail.booked_lab.is_booked = False
#         user_booking_detail.booked_lab.save()
#         user_booking_detail.delete()
#         return Response({"message":"Booked space deleted successfully"})
