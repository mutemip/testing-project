# from . import views
from django.urls import path 
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = "booking_manager_api"

booking_manager_urls = [
    # path('addlab/<int:slot_id>' , views.BookingsCreateView.as_view() , name = 'addLabs') ,
    # path('addslot' , views.CreateSlotView.as_view() , name = 'addSlot' ) ,
    # path('getAllBookedDates' , views.AllBookedDatesListView.as_view() , name = 'getAllBookedDates' ) ,
    # path('getAllBookedDates/<int:slot_id>' , views.SlotBookingDetailView.as_view() , name = 'getSlotBookingDetail' ) ,
    # path('getAllBookedDates/userBookingDetails/<int:booking_id>' , views.UserBookingDetailView.as_view() , name = 'userBookingDetail' ) ,
    

    path('create/entity/service/',views.EntityServiceView.as_view(),name='create_entity_service'),
    path('list/bookable/services/<str:type>/',views.BookableServiceView.as_view(),name='list_bookable_services'),
    path('bookable/service/<int:service_id>/',views.BookableServiceDetailView.as_view(),name='get_bookable_service_details'),
    path('entity/services/',views.EntityServiceListView.as_view(),name='entity_services'),


    path('week/days/',views.DaysOfTheWeekView.as_view(),name='days_of_teh_week'),
    path('time/slots/interval/<int:interval>/',views.TimeSlotAView.as_view(),name='time_slots_by_interval'),
    path('booking/schedule/',views.BookingScheduleView.as_view(),name='entity_booking_schedule'),
    path('entity/booking/schedules/',views.EntityBookingSchedules.as_view(),name='list_entity_booking_schedule'),

    path('list/booked/services/', views.ExternalEntityBookingView.as_view(),name="list_booked_services" ),
    path('dashboard/summary/', views.DashboardMetricsView.as_view(),name="dashboard_summary"),


    path('populate/bookable/service/', views.populate_bookable_service,name="populate_bookable_service" ),
]