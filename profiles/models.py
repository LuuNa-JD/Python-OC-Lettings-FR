from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    A Profile model that represent the User model with additional information.

    Attributes:
        user: A one-to-one relationship with the User model.
        favorite_city: An optional field to store the user's favorite city.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Returns the string representation of the Profile instance.
        """
        return self.user.username
