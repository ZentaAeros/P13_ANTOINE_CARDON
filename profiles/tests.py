from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile
import pytest

client = Client()


@pytest.mark.django_db
def test_profile():
    response = client.get(reverse('profiles:index'))
    assert '<title>Profiles</title>' in response.content.decode()


@pytest.mark.django_db
def test_profile_details():
    user = User.objects.create(username="jean")

    Profile.objects.create(user=user, favorite_city="USA")
    response = client.get(reverse('profiles:profile', kwargs={'username': 'jean'}))

    assert '<title>jean</title>' in response.content.decode()


def test_url_of_index_profile():
    path = reverse('profiles:index')
    assert path == '/profiles/'


def test_url_of_profile_details():
    path = reverse('profiles:profile', kwargs={'username': 'jeandupont'})
    assert path == '/profiles/jeandupont/'
