from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Favourite, Review
from fresh_basket.products.models import Product

User = get_user_model()


class CommonAppTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        image_file = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'',
            content_type='image/jpeg'
        )

        self.product = Product.objects.create(name='Test Product', price=10.0, image=image_file)

    def test_add_to_favorites_view(self):
        self.client.force_login(self.user)
        url = reverse('add-to-favourites', kwargs={'pk': self.product.pk})
        response = self.client.post(url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Favourite.objects.filter(user=self.user, product=self.product)), 1)

    def test_favorite_list_view(self):
        self.favourite1 = Favourite.objects.create(user=self.user, product=self.product)
        self.favourite2 = Favourite.objects.create(user=self.user, product=self.product)
        self.client.force_login(self.user)
        url = reverse('favourites-products')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/favourites-list.html')
        self.assertEqual(len(response.context['favourites']), 2)

    def test_remove_from_favorites_view(self):
        self.client.force_login(self.user)
        favourite = Favourite.objects.create(user=self.user, product=self.product)
        url = reverse('remove-from-favourites', kwargs={'pk': favourite.pk})
        response = self.client.post(url, follow=True)  # Add follow=True
        self.assertEqual(response.status_code, 200)  # Change status_code to 200
        self.assertEqual(len(Favourite.objects.filter(user=self.user, product=self.product)), 0)

    def test_product_reviews_list_view(self):
        url = reverse('product-reviews', kwargs={'pk': self.product.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/reviews-list.html')
        self.assertEqual(len(response.context['reviews']), 0)

    def test_add_review_to_product_view(self):
        self.client.force_login(self.user)
        url = reverse('product-reviews-add', kwargs={'pk': self.product.pk})
        data = {
            'content': 'Test review content',
            'rating': 4.5,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(Review.objects.filter(user=self.user, product=self.product)), 1)
