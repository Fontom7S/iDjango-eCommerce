from django.contrib.auth.models import User
from django.db import models

from admin_shop.models.city import City
from admin_shop.models.country import Country


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    Address = models.CharField(max_length=250)

    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    city = models.ForeignKey(City, on_delete=models.CASCADE)

    sex = models.TextChoices("Masculin", "Féminin")

    facebook_urls = models.URLField(blank=True)

    twitter_urls = models.URLField(blank=True)

    linkded_urls = models.URLField(blank=True)

    def __str__(self):
        return 'profile of ' + self.user.username
