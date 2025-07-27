from django.db import models

class Movie(models.Model):
    movie_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Rating(models.Model):
    user_id = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    rating = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user_id', 'movie')
