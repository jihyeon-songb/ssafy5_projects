from django.db.models import fields
from rest_framework import serializers
from .models import Collection, Movie, Genre
from accounts.serializers import UserSerializer

class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = '__all__'


class MoviesListSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('genres', 'star_rating_average',)


class CollectionListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Collection
        fields = '__all__'


class CollectionSerializer(serializers.ModelSerializer):
    movies_count = serializers.IntegerField(source='movies.count', read_only=True)

    class Meta:
        model = Collection
        fields = '__all__'
        read_only_fields = ('movies', 'user', )


class MoviesSerializer(serializers.ModelSerializer):
    collection_set = CollectionSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('genres', 'star_rating_average',)