from django.test import TestCase
from .models import MovieDetails


# Model Tests
class ModelTests(TestCase):
    def test(self):
        MovieDetails(name="Escuadron Suicida", genre="Accion", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla auctor nulla metus, vel ut.", director="James Gunn", year="2021").save()
        movie1 = MovieDetails.objects.get(name="Escuadron Suicida")
        self.assertEqual(movie1.name, "Escuadron Suicida")
        self.assertEqual(movie1.genre, "Accion")
        self.assertEqual(movie1.director, "James Gunn")