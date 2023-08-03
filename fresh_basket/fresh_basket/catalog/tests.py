from django.test import TestCase, Client
from django.urls import reverse
from .models import Catalog


class CatalogViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_catalog_view(self):
        Catalog.objects.create(name='All Products Catalog', description='Catalog Description')
        url = reverse('catalog')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/catalog.html')
        self.assertIn('all_catalogs', response.context)
        self.assertEqual(response.context['all_catalogs'].name, 'All Products Catalog')
        self.assertIsNone(response.context['discounted_catalogs'])

    def test_catalog_view_no_catalogs(self):
        Catalog.objects.all().delete()

        url = reverse('catalog')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/catalog.html')

        self.assertIsNone(response.context['all_catalogs'])
        self.assertIsNone(response.context['discounted_catalogs'])
