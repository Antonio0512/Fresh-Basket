from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from decimal import Decimal

from .models import CartItem
from fresh_basket.products.models import Product

User = get_user_model()


class ShoppingCartAppTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        image_file = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'',
            content_type='image/jpeg'
        )

        self.product = Product.objects.create(name='Test Product', price=10.0, image=image_file)

    def test_shopping_cart_view(self):
        self.client.force_login(self.user)
        url = reverse('shopping-cart')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shopping cart/shopping_cart.html')

    def test_add_to_cart_view(self):
        self.client.force_login(self.user)
        url = reverse('add-to-cart', kwargs={'pk': self.product.pk})

        data = {
            'quantity': '2',
            'weight': '1'
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

        cart_item = CartItem.objects.filter(user=self.user, product=self.product).first()
        self.assertIsNotNone(cart_item)
        self.assertEqual(cart_item.quantity, 2)
        self.assertEqual(cart_item.weight, Decimal('1'))

    def test_delete_from_cart_view(self):
        self.client.force_login(self.user)
        cart_item = CartItem.objects.create(user=self.user, product=self.product)
        url = reverse('delete-from-cart', kwargs={'pk': cart_item.pk})
        response = self.client.post(url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(CartItem.objects.filter(user=self.user, product=self.product)), 0)
