

from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the home page!")


