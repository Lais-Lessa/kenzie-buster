from django.db import models
from movies.models import Movie
from users.models import User

class MovieOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movie_orders')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_orders')
    purchased_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __repr__(self) -> str:
        return f"<Movie Order - id: {self.id}, price: {self.title}, buyed at: {self.purchased_at}>"
