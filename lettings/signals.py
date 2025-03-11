import logging
import sentry_sdk
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Letting

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Letting)
def log_letting_save(sender, instance, created, **kwargs):
    """
    Capture les créations et modifications des locations.
    """
    if created:
        message = f"Une nouvelle location a été ajoutée : {instance.title}"
    else:
        message = f"La location '{instance.title}' a été modifiée."

    logger.info(message)
    sentry_sdk.capture_message(message)


@receiver(post_delete, sender=Letting)
def log_letting_delete(sender, instance, **kwargs):
    """
    Capture la suppression d'une location.
    """
    message = f"La location '{instance.title}' a été supprimée."
    logger.warning(message)
    sentry_sdk.capture_message(message)
