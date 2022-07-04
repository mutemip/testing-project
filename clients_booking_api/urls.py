from django.urls import path
from . import views

app_name = "clients_booking_api"

clients_booking_urls = [
    # path('bookings/', views.ClientBookingCreateView.as_view(), name='booking'),
    
    path('possible/bookings/<int:service_id>/<str:booking_date>/', views.PossibleBookingTimeSlots.as_view(), name='possible_bookings'),
    path('create/booking/', views.CreateBooking.as_view(), name='create_booking'),
    path('list/services/booked/', views.ListPatientBookedServiceView.as_view(), name='list_patient_booked_services'),
    # path('list/services/booked/', views.ListPatientBookedServiceView.as_view(), name='list_patient_booked_services'),
    path('get/user/book/service/<int:user_book_service_id>/', views.GetUserBookServiceView.as_view(), name='client_get_user_booke_service'),

    path('list/entity/services/', views.ClientEntityServiceListView.as_view(), name='client_list_entity_services'),
]
