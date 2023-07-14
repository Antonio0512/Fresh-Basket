from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from .models import Product
from ..catalog.models import Catalog


class ProductModelTest(TestCase):
    def setUp(self):
        self.catalog = Catalog.objects.create(name='Discount Catalog')

        image_file = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'',
            content_type='image/jpeg'
        )

        self.product = Product.objects.create(
            name='Test Product',
            price=10.0,
            image=image_file
        )
        self.product.discount_catalog = self.catalog
        self.product.save()

    def test_all_products_list_view(self):
        url = reverse('products-all')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/all_products.html')
        self.assertContains(response, self.product.name)

    def test_discount_products_list_view(self):
        url = reverse('products-discount')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/discount_products.html')
        self.assertContains(response, self.product.name)

    def test_product_details_view(self):
        url = reverse('all-product-details', kwargs={'pk': self.product.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_details.html')
        self.assertContains(response, self.product.name)

    def test_product_discount_catalog(self):
        self.assertEqual(self.product.discount_catalog, self.catalog)

    def test_product_has_discount_catalog(self):
        self.assertTrue(self.product.discount_catalog)

    def test_product_discount_catalog_name(self):
        self.assertEqual(self.product.discount_catalog.name, 'Discount Catalog')

    def test_product_without_discount_catalog(self):
        product_without_discount = Product.objects.create(
            name='Product Without Discount',
            price=20.0,
        )
        self.assertIsNone(product_without_discount.discount_catalog)

