from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.contrib import admin
from django.urls import path, include
from rpc_client_app.urls import rpc_client_app_urls
from intel_api.urls import intel_urls
from booking_manager_api.urls import booking_manager_urls
from clients_booking_api.urls import clients_booking_urls

from intel_rpc_server.services.userbookservice.handlers import grpc_handlers as userbookservice_handlers

schema_view = get_schema_view(
   openapi.Info(
      title="PanaBIOS Intel API",
      default_version='v1',
      description="Booking services",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('docs/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),


    path('api/v1/intel/', include((intel_urls, 'intal_api'), namespace='intel_api')),
    path('api/v1/booking/manager/', include((booking_manager_urls, 'manager_booking_api'), namespace='manager_booking_api')),
    path('api/v1/booking/client/', include((clients_booking_urls, 'clients_booking_api'), namespace='clients_booking_api')),
    

    path('rpc/client/', include((rpc_client_app_urls, 'rpc-client-app'), namespace='rpc_client_app')),
]

def grpc_handlers(server):
   userbookservice_handlers(server)