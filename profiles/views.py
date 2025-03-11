import logging
import sentry_sdk
from django.shortcuts import render, get_object_or_404
from .models import Profile

logger = logging.getLogger(__name__)


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed consequat libero
# pulvinar eget. Fusc faucibus, urna quis auctor pharetra,
# massa dolor cursus neque, quis dictum lacus d
def index(request):
    """
    Vue affichant la liste des profils.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    logger.info("Liste des profils récupérée avec succès.")
    return render(request, 'profiles/index.html', context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate.
# Sed tincidunt, dolor id facilisis fringilla, eros leo tristique lacus,
# it. Nam aliquam dignissim congue.
# Pellentesque habitant morbi tristique senectus et netus et males
def profile(request, username):
    """
    Vue affichant les détails d'un profil utilisateur.
    """
    try:
        profile = get_object_or_404(Profile, user__username=username)
        context = {'profile': profile}
        logger.info(f"Profil chargé : {profile.user.username}")
        return render(request, 'profiles/profile.html', context)
    except Exception as e:
        sentry_sdk.capture_exception(e)
        logger.error(f"Erreur lors de l'affichage du profil {username}: {e}")
        return render(request, "500.html", status=500)
