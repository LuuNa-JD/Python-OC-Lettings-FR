import logging
import sentry_sdk
from django.shortcuts import render

logger = logging.getLogger(__name__)


# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie quam lobortis leo
# consectetur ullamcorper non id est. Praesent dictum, nulla eget feugiat sagittis, sem mi
# convallis eros, vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum, eget
# consequat ipsum lobortis quis. Phasellus eleifend ex auctor venenatis tempus. Aliquam vitae
# erat ac orci placerat luctus. Nullam elementum urna nisi, pellentesque iaculis enim cursus in.
# Praesent volutpat porttitor magna, non finibus neque cursus id.
def index(request):
    """
    Vue affichant la page d'accueil.
    """
    try:
        logger.info("Page d'accueil affichée.")
        return render(request, 'index.html')
    except Exception as e:
        logger.error(f"Erreur lors de l'affichage de la page d'accueil: {str(e)}")
        sentry_sdk.capture_exception(e)
        return render(request, "500.html", status=500)


def custom_404(request, exception):
    """
    Vue personnalisée pour gérer les erreurs 404.
    Returns:
        HttpResponse: Page HTML personnalisée d'erreur 404.
    """
    logger.warning(f"Page 404 - URL introuvable: {request.path}")
    return render(request, "404.html", status=404)


def custom_500(request):
    """
    Vue personnalisée pour gérer les erreurs 500.
    Returns:
        HttpResponse: Page HTML personnalisée d'erreur 500.
    """
    logger.error("Erreur 500 - Erreur interne du serveur")
    sentry_sdk.capture_message("Erreur serveur détectée", level="error")
    return render(request, "500.html", status=500)
