from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('reset-password', views.reset_password, name='reset_password'),
    path('<int:movie_id>', views.details, name='details'),
    path('<int:movie_id>/watch', views.watch, name='watch'),
    path('<int:movie_id>/rate', views.rate, name='rate'),
    path('<int:movie_id>/add', views.add_to_list, name='add_to_list'),
    path('<int:movie_id>/remove', views.remove_from_list, name='remove_from_list'),
    path('profile', views.profile, name='profile'),
    path('orders', views.orders, name='orders'),
]
