from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta

from .models import Movie, Order


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    title = 'All movies list'
    context = {
        'title': title,
        'movies': movies,
    }

    return render(request, 'movies/index.html', context)


@login_required(login_url='/login')
def details(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(
        request,
        'movies/details.html',
        {
            'movie': movie,
            'user': {
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
            }
        })


@login_required(login_url='/login')
def watch(request, movie_id):
    print(request.user.id, movie_id)
    order = Order.objects.filter(
        user_id=request.user.id,
        movie_id=movie_id,
        date__gte=datetime.now() - timedelta(days=1)
    )

    if order.first() is None:
        Order.objects.create(user=request.user, movie_id=movie_id)

    return render(request, 'movies/watch.html', {
        'movie': Movie.objects.get(pk=movie_id),
    })


def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    print(user, username, password)

    if user is not None:
        login(request, user)
        return redirect(to='/')
    else:
        return render(request, 'movies/login.html', {'error': 'Invalid credentionals'})


def reset_password(request):
    return render(request, 'movies/reset_password.html')


def rate(request):
    return render(request, 'movies/placeholder.html')


def add_to_list(request):
    return render(request, 'movies/placeholder.html')


def remove_from_list(request):
    return render(request, 'movies/placeholder.html')


@login_required(login_url='/login')
def orders(request):
    orders = Order.objects.filter(user_id=request.user.id)

    return render(request, 'movies/orders.html', {'orders': orders})


def profile(request):
    return render(request, 'movies/placeholder.html')
