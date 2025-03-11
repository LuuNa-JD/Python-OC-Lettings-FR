import logging
from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator

logger = logging.getLogger(__name__)


class Address(models.Model):
    """
    Modèle représentant une adresse.

    Attributes:
        number (PositiveIntegerField): Numéro de l'adresse.
        street (CharField): Nom de la rue.
        city (CharField): Ville de l'adresse.
        state (CharField): État ou région.
        zip_code (CharField): Code postal.
        country_iso_code (CharField): Code ISO du pays (ex: 'FR' pour France).
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        logger.info(f"Nouvelle adresse ajoutée: {self}")

    def __str__(self):
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Modèle représentant une location.

    Attributes:
        title (CharField): Titre de la location.
        address (OneToOneField): Référence à l'adresse associée à cette location.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        logger.info(f"Nouvelle location ajoutée: {self.title}")

    def __str__(self):
        return self.title
