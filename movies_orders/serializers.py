from movies.models import Movie
from movies_orders.models import MovieOrder
from rest_framework import serializers

class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.ReadOnlyField(source='movie.title', read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    purchased_by = serializers.ReadOnlyField(source='user.email', read_only=True)
    purchased_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data: dict) -> MovieOrder:
        return MovieOrder.objects.create(**validated_data)
