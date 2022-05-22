from django.shortcuts import render
from .models import Movie

def home(request):
    searchTerm = request.GET.get('searchMovie')
    return render(request, 'home.html', {'searchTerm':searchTerm})

def movie_list(request):
    searchTerm = request.GET.get('searchTerm')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'searchTerm':searchTerm, 'movies': movies})