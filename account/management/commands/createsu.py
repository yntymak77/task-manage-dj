from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="admintask1").exists():
            supassword= os.environ['SU_PASSWORD']
            User.objects.create_superuser("admintask1", "adminofficial@gmail.com", supassword)
