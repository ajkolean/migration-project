from django.db import models

# Create your models here.


class Food(models.Model):
    HEALTH_SCORE = (
        (0, 'Healthy'),
        (1, 'Average'),
        (2, 'Unhealthy'),
    )
    type = models.TextField()
    country = models.CharField(max_length=50)
    healthiness = models.IntegerField(default=1, choices=HEALTH_SCORE)


class Restaurant(models.Model):
    DERR_SCORE = (
        (0, 'Terrible'),
        (1, 'Bad'),
        (2, 'Average'),
        (3, 'Good'),
        (4, 'Amazing'),
    )
    name = models.CharField(max_length=50, null=True, blank=True)
    type = models.ForeignKey('Food', related_name='restaurants')
    daysopen = models.TextField()
    location = models.TextField()
    derrscore = models.FloatField()
    website = models.URLField(max_length=200, null=True, blank=True)
