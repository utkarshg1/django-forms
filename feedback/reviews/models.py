from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    user_name = models.CharField(max_length=50)
    review_text = models.TextField(max_length=200)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MinValueValidator(5)])
