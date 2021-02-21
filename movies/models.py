from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User


# Create your models here.
class Director(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=160)
    birth = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.ForeignKey(Director, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)
    length = models.FloatField()
    poster = models.ImageField(upload_to='posters/', null=True)
    description = models.TextField(null=True)
    create_date = models.DateField()

    def add_bookmark(self, user):
        bookmark = Bookmarks.objects.get_or_create(movie=self, user=user)
        bookmark.save()
        return bookmark

    def remove_bookmark(self, user):
        try:
            bookmark = Bookmarks.objects.get(movie=self, user=user)
            bookmark.delete()
        except Exception as e:
            return None

    def rate(self, user, rate):
        rating = Ratings.objects.get_or_create(movie=self, user=user)
        rating.rate = rate
        rating.save()
        return rating

    def avg_rate(self):
        return self.ratings_set.all().aggregate(Avg('rate'));

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
    rate = models.PositiveSmallIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.movie} ({self.user}, {self.ratio})'
