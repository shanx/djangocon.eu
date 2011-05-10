from django.db import models

from model_utils import Choices
from sorl.thumbnail import ImageField

class Sponsor(models.Model):
    LEVEL = Choices(
        (0, 'kryptonite', 'Kryptonite'),
        (1, 'diamond', 'Diamond'),
        (2, 'platinum', 'Platinum'),
        (3, 'gold', 'Gold'),
        (4, 'producer', 'Producer'))
    name = models.CharField(max_length=100)
    level = models.IntegerField(choices=LEVEL, default=LEVEL.kryptonite)
    url = models.URLField()
    image = ImageField(upload_to='sponsors')
    about = models.TextField(blank=True, null=True)

