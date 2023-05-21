from django.test import Client
from django.urls import reverse

client = Client()


def test_homepage():
    response = client.get(reverse('home:index'))
    assert '<title>Holiday Homes</title>' in response.content.decode()


def test_homepage_url():
    path = reverse('home:index')
    assert path == '/'
