import pytest
from django.urls import reverse
from lettings.models import Letting, Address


@pytest.mark.django_db
def test_address_model():
    """
    Vérifie que l'objet Address est correctement créé et affiché.
    """
    address = Address.objects.create(
        number=123, street="Rue de Paris", city="Paris",
        state="Île-de-France", zip_code="75000", country_iso_code="FR"
    )
    assert str(address) == "123 Rue de Paris"


@pytest.mark.django_db
def test_letting_model():
    """
    Vérifie que l'objet Letting est correctement créé et affiché.
    """
    address = Address.objects.create(
        number=456, street="Boulevard Haussmann", city="Paris",
        state="Île-de-France", zip_code="75008", country_iso_code="FR"
    )
    letting = Letting.objects.create(title="Appartement Parisien", address=address)
    assert str(letting) == "Appartement Parisien"


@pytest.mark.django_db
def test_lettings_index_view(client):
    """
    Teste que la page des locations renvoie un code 200.
    """
    url = reverse('lettings:index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_letting_detail_view(client):
    """
    Teste qu'une location spécifique est accessible.
    """
    address = Address.objects.create(
        number=456, street="Boulevard Haussmann", city="Paris",
        state="Île-de-France", zip_code="75008", country_iso_code="FR"
    )
    letting = Letting.objects.create(title="Appartement Haussmannien", address=address)
    url = reverse('lettings:letting', kwargs={'letting_id': letting.id})
    response = client.get(url)
    assert response.status_code == 200
