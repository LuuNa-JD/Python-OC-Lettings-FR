import logging
import sentry_sdk
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profile

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Profile)
def log_profile_save(sender, instance, created, **kwargs):
    """
    Capture les créations et modifications des profils.
    """
    if created:
        message = f"Un nouveau profil a été créé : {instance.user.username}"
    else:
        message = f"Le profil de {instance.user.username} a été modifié."

    logger.info(message)
    sentry_sdk.capture_message(message)


@receiver(post_delete, sender=Profile)
def log_profile_delete(sender, instance, **kwargs):
    """
    Capture la suppression d'un profil.
    """
    message = f"Le profil de {instance.user.username} a été supprimé."
    logger.warning(message)
    sentry_sdk.capture_message(message)
