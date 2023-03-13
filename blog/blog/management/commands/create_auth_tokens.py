from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class Command(BaseCommand):
    help = 'Creates initial authtokens'

    def handle(self, *args, **options):
        User = get_user_model()
        for user in User.objects.all():
            token = Token.objects.get_or_create(user=user)


    
    