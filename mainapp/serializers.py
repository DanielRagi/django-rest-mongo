'''
@Author: 
'''

from .models import MovieDetails
from rest_framework import serializers

# Create a class that links movies details with the serializer
# serializer -> convert data to json string


class SerializeMovie(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MovieDetails
        fields = ('id', 'name', 'genre', 'description', 'director', 'year')
