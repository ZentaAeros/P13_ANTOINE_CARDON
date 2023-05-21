from django.test import Client
from django.urls import reverse
from lettings.models import Letting, Address
import pytest

client = Client()


@pytest.mark.django_db
def test_letting():
    response = client.get(reverse('lettings:index'))
    assert '<title>Lettings</title>' in response.content.decode()


@pytest.mark.django_db
def test_letting_details():
    address = Address.objects.create(
        number=1234,
        street="street name",
        city="city name",
        state="state name",
        zip_code=123456,
        country_iso_code="ABC"
    )
    Letting.objects.create(title="letting title", address=address)
    response = client.get(reverse('lettings:letting', kwargs={'letting_id': 1}))

    assert '<title>letting title</title>' in response.content.decode()


def test_url_of_letting():
    path = reverse('lettings:index')
    assert path == '/lettings/'


def test_url_of_letting_details():
    path = reverse('lettings:letting', kwargs={'letting_id': 1})
    assert path == '/lettings/1/'
