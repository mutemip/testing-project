from django.core.management.base import BaseCommand

from booking_manager_api.models import BookableService


class Command(BaseCommand):
    help = "Load Bookable Services"

    def handle(self, *args, **options):
        BookableService.load_bookable_service()
