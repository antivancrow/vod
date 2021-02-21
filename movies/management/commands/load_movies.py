from django.core.management.base import BaseCommand
from movies.models import *
import yaml


class Command(BaseCommand):
    help = 'Load movies fixture'

    def handle(self, *args, **kwargs):
        with open('fixtures/movies.yaml') as f:
            data = yaml.safe_load(f)
            for m in data['movies']:
                director = Director.objects.get_or_create(first_name=m['director']['first_name'], last_name=m['director']['last_name'])[0]
                director.birth = m['director']['birth']
                director.save()

                movie = Movie.objects.get_or_create(title=m['title'])[0]
                movie.director = director
                movie.poster = m['poster']
                movie.year = m['year']
                movie.save()

                for c in m['category']:
                    category = Category.objects.get_or_create(name=c)[0]
                    category.save()
                    movie.category = category
                    movie.save()

                print(f'{movie.title} ({movie.year}): added')


