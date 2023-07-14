from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse

from django.utils import timezone
from datetime import timedelta

from fresh_basket.promotions.models import Promotions

User = get_user_model()


class UserRegisterViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('register')
        self.data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'Newpassword1',
            'password2': 'Newpassword1'
        }

    def test_user_register_view_success(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('page-home'))

        self.assertTrue(User.objects.filter(username='newuser').exists())

        # Additional assertions to verify user authentication
        user = User.objects.get(username='newuser')
        self.assertTrue(user.is_authenticated)
        self.assertEqual(self.client.session['_auth_user_id'], str(user.id))

        # Additional assertions to verify user model fields
        self.assertEqual(user.username, 'newuser')
        self.assertEqual(user.email, 'newuser@example.com')

    def test_user_register_view_password_mismatch(self):
        self.data['password2'] = 'Password2'  # Different password
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'password2', 'The two password fields didn’t match.')

    def test_user_register_view_invalid_email(self):
        self.data['email'] = 'invalid_email'
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')

    def test_user_register_view_missing_required_fields(self):
        del self.data['email']
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'email', 'This field is required.')

        del self.data['username']
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'username', 'This field is required.')

    def test_user_register_view_duplicate_email(self):
        User.objects.create_user(username='existinguser', email='newuser@example.com', password='Existingpassword')
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'email', 'User with this Email already exists.')


class UserLoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='Testpassword')

    def test_user_login_view_success(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

        data = {
            'username': 'testuser',
            'password': 'Testpassword',
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('page-home'))

        # Additional assertions to verify user authentication
        self.assertTrue(self.user.is_authenticated)
        self.assertEqual(self.client.session['_auth_user_id'], str(self.user.id))

    def test_user_login_view_invalid_credentials(self):
        url = reverse('login')
        data = {
            'username': 'testuser',
            'password': 'Invalidpassword',
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
        self.assertContains(response, 'Invalid username or password. Please try again.')

        # Additional assertions to verify user authentication
        self.assertFalse(response.wsgi_request.user.is_authenticated)
        self.assertNotIn('_auth_user_id', self.client.session)


class UserLogoutViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='Testpassword')

    def test_user_logout_view(self):
        # Log in the user
        self.client.force_login(self.user)

        # Access the logout view
        url = reverse('logout')
        response = self.client.get(url)

        # Check the response
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/logout.html')

        # Check the user authentication status
        self.assertTrue(response.wsgi_request.user.is_authenticated)

        # Log out the user
        response = self.client.post(url)

        # Check the response
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('page-home'))

        # Check the user authentication status after logout
        self.assertFalse(response.wsgi_request.user.is_authenticated)
        self.assertIsInstance(response.wsgi_request.user, AnonymousUser)


class UserDetailsViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='testuser@example.com',
            first_name='Test',
            last_name='User',
            profile_picture=None,
            gender='Male'
        )
        self.promotion = Promotions.objects.create(
            title='Test Promotion',
            description='Test promotion',
            start_date=timezone.now(),
            end_date=timezone.now() + timedelta(days=7)
        )

    def test_user_details_view(self):
        self.client.force_login(self.user)
        url = reverse('profile-details', kwargs={'pk': self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile-details.html')
        self.assertContains(response, self.user.username)

        # Additional assertions to verify context data
        self.assertQuerysetEqual(
            response.context['promotions'],
            ['Test Promotion'],
            transform=str
        )


class UserEditViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='testuser@example.com',
            first_name='Test',
            last_name='User',
            profile_picture=None,
            gender='Male'
        )
        self.promotion = Promotions.objects.create(
            title='Test Promotion',
            description='Test promotion',
            start_date=timezone.now(),
            end_date=timezone.now() + timedelta(days=7)
        )

    def test_user_edit_view_success(self):
        self.client.force_login(self.user)
        url = reverse('profile-edit', kwargs={'pk': self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile-edit.html')

        data = {
            'username': 'newusername',
            'email': 'newemail@example.com',
            'first_name': 'New',
            'last_name': 'Name',
            'gender': 'Female',
            'profile_picture': '',
        }

        response = self.client.post(url, data=data)
        self.assertRedirects(response, reverse('profile-details', kwargs={'pk': self.user.pk}))

        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'newusername')
        self.assertEqual(self.user.email, 'newemail@example.com')
        self.assertEqual(self.user.first_name, 'New')
        self.assertEqual(self.user.last_name, 'Name')
        self.assertEqual(self.user.gender, 'Female')

    def test_user_edit_view_invalid_form(self):
        self.client.force_login(self.user)
        url = reverse('profile-edit', kwargs={'pk': self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile-edit.html')

        data = {
            'username': '',
            'email': 'newemail@example.com',
            'first_name': 'New',
            'last_name': 'Name',
            'gender': 'Female',
            'profile_picture': '',
        }

        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile-edit.html')

        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Error updating profile.')

        self.user.refresh_from_db()
        self.assertNotEqual(self.user.email, 'newemail@example.com')


class UserDeleteViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='testuser@example.com',
        )
        self.client.force_login(self.user)

    def test_user_delete_view_success(self):
        url = reverse('profile-delete', kwargs={'pk': self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile-delete.html')

        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('register'))
        self.assertFalse(User.objects.filter(username='testuser').exists())

    def test_user_delete_view_get_context_data(self):
        url = reverse('profile-delete', kwargs={'pk': self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, str(self.user))
