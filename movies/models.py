from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User


# Create your models here.
class Director(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=160)
    birth = models.DateField(null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.ForeignKey(Director, on_delete=models.DO_NOTHING, null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)
    year = models.PositiveSmallIntegerField(null=True)
    poster = models.ImageField(upload_to='posters/', null=True)
    description = models.TextField(null=True)

    def add_bookmark(self, user):
        bookmark = Bookmarks.objects.get_or_create(movie_id=self.id, user_id=user.id)[0]
        bookmark.save()
        return bookmark

    def remove_bookmark(self, user):
        try:
            bookmark = Bookmarks.objects.get(movie_id=self.id, user_id=user.id)[0]
            bookmark.delete()
        except Exception as e:
            return None

    def is_bookmarked(self, user):
        try:
            Bookmarks.objects.get(movie_id=self.id, user_id=user.id)[0]
            return True
        except Exception as e:
            return False

    def add_rate(self, user, rate):
        rating = Ratings.objects.get_or_create(movie_id=self.id, user_id=user.id)[0]
        rating.rate = rate
        rating.save()
        return rating

    def is_rated(self, user):
        try:
            Ratings.objects.get(movie=self, user=user)[0]
            return True
        except Exception as e:
            return False

    def avg_rate(self):
        return self.ratings_set.all().aggregate(Avg('rate'))['rate__avg']

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} / {self.movie} / {self.date}'


class Bookmarks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.movie} ({self.date})'


class Ratings(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.movie} ({self.user}, {self.rate})'
