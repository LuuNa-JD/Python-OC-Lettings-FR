import logging
from django.db import models
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)


class Profile(models.Model):
    """
    Modèle représentant le profil utilisateur.

    Attributes:
        user (OneToOneField): Référence à l'utilisateur Django.
        favorite_city (CharField): Ville préférée de l'utilisateur (optionnelle).
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def save(self, *args, **kwargs):
        logger.info(f"Profil utilisateur mis à jour: {self.user.username}")
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Retourne le nom d'utilisateur comme représentation en chaîne de caractères du profil.
        """
        return self.user.username
