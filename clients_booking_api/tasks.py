# from celery.decorators import task
# from celery.utils.log import get_task_logger
# import logging
# import requests
# from booking_manager_api.models.util import get_object_or_none
# from django.conf import settings
# import json



# logger = get_task_logger(__name__)

# RWANDA = "Rwanda"


# @task(name="send_booking_info_to_country")
# def send_booking_info_to_country(self,userbookservice_id,data):
#     from clients_booking_api.models.bookservice import UserBookService,UserBookTravelInformation
#     bookedservice = get_object_or_none(UserBookService,id=userbookservice_id)
#     if bookedservice:
#         if bookedservice.is_sharing_enabled():
#             external_entity_country = bookedservice.booked_entity_service.bookable_entity.detail.country
#             if external_entity_country == "Ghana":#RWANDA
#                 auth_endpoint = settings.RWANDA_TOKEN_URL
#                 booking_post_url =  settings.RWANDA_BOOKING_ENDPOINT_URL
                
#                 payload = {
#                     "username": settings.RWANDA_USERNAME,
#                     "password": settings.RWANDA_PASSWORD
#                 }
#                 headers = {"Content-Type": "application/json"}
#                 response = requests.post(url=auth_endpoint, json=payload, headers=headers)

#                 res_data = json.loads(response.text)
#                 # if res_data['token']:

#     pass