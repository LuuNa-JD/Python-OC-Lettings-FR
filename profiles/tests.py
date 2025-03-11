import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from profiles.models import Profile


@pytest.mark.django_db
def test_profile_model():
    """
    Vérifie que l'objet Profile est correctement créé et affiché.
    """
    user = User.objects.create(username="TestUser")
    profile = Profile.objects.create(user=user, favorite_city="Lyon")
    assert str(profile) == "TestUser"


@pytest.mark.django_db
def test_profiles_index_view(client):
    """
    Teste que la page des profils renvoie un code 200.
    """
    url = reverse('profiles:index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_profile_detail_view(client):
    """
    Teste qu'un profil utilisateur est accessible.
    """
    user = User.objects.create(username="ProfileUser")
    Profile.objects.create(user=user, favorite_city="Marseille")
    url = reverse('profiles:profile', kwargs={'username': "ProfileUser"})
    response = client.get(url)
    assert response.status_code == 200
