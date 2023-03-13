from django.contrib.auth.models import User
import lorem
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
import random
from content.models import Post,PostComment


class Command(BaseCommand):
    help = 'Generates some fixtures we can demo with'

    def handle(self, *args, **options):
        User = get_user_model()
        usernames = [
            'Higherit',
            'DariSun',
            'RaeRocket',
            'ChiquitaMajere',
            'Lamarket',
            'GoldenReader',
            'Fangfe',
            'Lamarket',
            'Lamarket',
            'Cuecardsh',
            'Communiquestaf',
            'Readerenes',
            'Spoiledic',
            'Discoverahon',
            'Sushydr',
            'FuzzyGrim',
            'Nexoneoft',
            'Gleediatr'
        ]

        posts = []
        # create root user
        root_user = User.objects.create_superuser(email="test@test.com", username='root', password='password')
        for username in random.sample(usernames, 6):
            user, created = User.objects.get_or_create(username=username, password='password')
            numposts = random.randrange(1,4)
            for i in range(numposts):
                post = Post.objects.create(title=lorem.sentence(), text=lorem.text(), author=user)
                posts.append(post)


        for username in random.sample(usernames, 12):
            user, created = User.objects.get_or_create(username=username, password='password')
            for i in range(random.randrange(1,12)):
                p = random.choice(posts)
                PostComment.objects.create(post=p, author=user, text=lorem.sentence())

