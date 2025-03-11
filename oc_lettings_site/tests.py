import pytest
from django.urls import reverse
from django.test import RequestFactory
from oc_lettings_site.views import custom_500, custom_404


@pytest.mark.django_db
def test_index_view(client):
    """
    Teste que la page d'accueil renvoie un code 200 et charge le bon template.
    """
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
    assert b"Welcome" in response.content


@pytest.mark.django_db
def test_custom_404_direct():
    """
    Teste que la vue custom_404 renvoie une réponse 404
    même quand on lui passe explicitement un paramètre 'exception'.
    """
    factory = RequestFactory()
    request = factory.get('/')
    exception = ValueError("Erreur 404 forcée")
    response = custom_404(request, exception)

    assert response.status_code == 404
    content = response.content.decode()
    assert "Oups" in content or "existe pas" in content


@pytest.mark.django_db
def test_custom_500_view():
    """
    Teste que la vue custom_500 renvoie une réponse 500 avec le contenu attendu.
    """
    factory = RequestFactory()
    request = factory.get('/')
    response = custom_500(request)

    assert response.status_code == 500
    content = response.content.decode()
    assert "Désolé" in content or "Erreur interne" in content
