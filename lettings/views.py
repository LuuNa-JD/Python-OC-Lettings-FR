import logging
import sentry_sdk
from django.shortcuts import render, get_object_or_404
from .models import Letting

logger = logging.getLogger(__name__)


# Aenean leo magna, vestibulum et tincidunt fermentum,
# consectetur quis velit. Sed non placerat massa. Integer est nunc, pulvinar a
# tempor et, bibendum id arcu. Vestibulum ante ipsum primis in faucibus
# orci luctus et ultrices posuere cubilia curae; Cras eget scelerisque
def index(request):
    """
    Vue affichant la liste des locations.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    logger.info("Liste des locations récupérée avec succès.")
    return render(request, 'lettings/index.html', context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non.
# In accumsan porta nisl id eleifend. Praesent dignissim,
# odio eu consequat pretium, purus urna vulputate arcu, vitae efficitur
#  lacus justo nec purus. Aenean finibus faucibus lectus at porta.
# Maecenas auctor, est ut luctus congue, dui enim mattis enim,
# ac condimentum velit libero in magna. Suspendisse potenti.
# In tempus a nisi sed laoreet.
# Suspendisse porta dui eget sem accumsan interdum.
# Ut quis urna pellentesque justo mattis ullamcorper ac non tellus.
# In tristique mauris eu velit fermentum, tempus pharetra est luctus.
# Vivamus consequat aliquam libero, eget bibendum lorem. Sed non dolor risus.
# Mauris condimentum auctor elementum. Donec quis nisi ligula.
# Integer vehicula tincidunt enim, ac lacinia augue pulvinar sit amet.
def letting(request, letting_id):
    """
    Vue affichant les détails d'une location spécifique.
    """
    try:
        letting = get_object_or_404(Letting, id=letting_id)
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        logger.info(f"Chargement de la location : {letting.title}")
        return render(request, 'lettings/letting.html', context)
    except Exception as e:
        sentry_sdk.capture_exception(e)
        logger.error(f"Erreur lors de l'affichage du letting {letting_id}: {e}")
        return render(request, "500.html", status=500)
