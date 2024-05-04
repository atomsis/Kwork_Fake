from django.shortcuts import redirect
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class AccountsViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_register_view_GET(self):
        client = Client()
        response = client.get(reverse('account:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')


    def tearDown(self):
        User.objects.filter(username='testuser').delete()

class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('account:register')
        self.login_url = reverse('account:login')
        self.username = 'testuser'
        self.password = 'testpassword'

    def test_user_login_after_registration(self):
        # Регистрируем нового пользователя
        response = self.client.post(self.register_url, {
            'username': self.username,
            'password1': self.password,
            'password2': self.password,
            'name': 'Test User',
            'contact_info': 'test@test.com',
            'experience': 'Some experience'
        })
        self.assertEqual(response.status_code, 302)  # Успешный редирект после регистрации

        # Пытаемся войти с данными нового пользователя
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': self.password,
        }, follow=True)  # Переходим по редиректу
        self.assertTrue(response.context['user'].is_authenticated)  # Пользователь залогинен
        self.assertRedirects(response, reverse('profile:customer_profile'))  # Перенаправление на главную страницу


